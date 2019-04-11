import time

from spider.config import INDEX_URL, MAX_FAILED_TIME, VALID_STATUSES
from spider.module.getter import Getter

from spider.module.mymysql import MySQL
from spider.module.myredis import RedisQueue
from spider.module.parser import Parser
from spider.utils.myrequest import MyRequest


class Schedule:
    queue = RedisQueue()
    db = MySQL()
    getter = Getter()
    parser = Parser()

    def start(self):
        index_request = MyRequest(url=INDEX_URL, callback=self.parser.parse_index, need_proxy=True)
        self.queue.put(index_request)

    def error(self, myrequest):
        """
        错误处理
        :param myrequest: MyRequest请求
        :return: None
        """
        myrequest.fail_time = myrequest.fail_time + 1
        print('Request Failed', myrequest.fail_time, 'Times:', myrequest.url)
        if myrequest.fail_time < MAX_FAILED_TIME:
            self.queue.put(myrequest)

    def schedule(self):
        """
        调度请求
        :return: None
        """
        while not self.queue.empty():
            time.sleep(5)
            myrequest = self.queue.get()
            try:
                callback = myrequest.callback
                print('Schedule', myrequest.url)
                response = self.getter.request(myrequest)
                if response and response.status_code in VALID_STATUSES:
                    results = callback(response)
                    if results:
                        for result in results:
                            print('New Result', type(result))
                            if isinstance(result, MyRequest):
                                self.queue.put(result)
                            if isinstance(result, dict):
                                self.db.insert(result)
                    else:
                        self.error(myrequest)
                else:
                    self.error(myrequest)
            except Exception as e:
                print('ERROR:', e.args)
                self.error(myrequest)

    def run(self):
        """
        启动爬虫
        :return:
        """
        self.start()
        self.schedule()


if __name__ == '__main__':
    schedule = Schedule()
    schedule.run()
