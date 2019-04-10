import pickle

from redis import StrictRedis

from spider.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY
from spider.utils.myrequest import MyRequest


class RedisQueue:
    def __init__(self):
        """
        初始化Redis
        """
        self.db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def put(self, myrequest):
        """
        向队列添加序列化后的MyRequest
        :param myrequest: 请求对象
        :return: 添加结果
        """
        if isinstance(myrequest, MyRequest):
            return self.db.rpush(REDIS_KEY, pickle.dumps(myrequest))
        return False

    def get(self):
        """
        取出下一个MyRequest并反序列化
        :return: MyRequest对象
        """
        if self.db.llen(REDIS_KEY):
            return pickle.loads(self.db.lpop(REDIS_KEY))
        else:
            return None

    def clear(self):
        self.db.delete(REDIS_KEY)

    def empty(self):
        return self.db.llen(REDIS_KEY) == 0
