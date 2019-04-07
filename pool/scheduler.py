import time
from multiprocessing import Process

from pool.module.api import app
from pool.module.getter import Getter
from pool.module.tester import Tester

TESTER_CYCLE = 20
GETTER_CYCLE = 20
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

API_HOST = '127.0.0.1'
API_PORT = '5000'


class Scheduler:
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        :param cycle: 休眠时间
        :return: None
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        :param cycle: 休眠时间
        :return: None
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启Web API
        :return: None
        """
        app.run(host=API_HOST, port=API_PORT)

    def run(self):
        print('代理池开始运行')
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter())
            getter_process.start()

        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester())
            tester_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api())
            api_process.start()
