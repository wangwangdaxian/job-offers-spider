import requests
from requests import ReadTimeout

from spider.module.myproxy import MyProxy


class Getter:
    def __init__(self):
        self.proxy = MyProxy()

    def request(self, my_request):
        """
        执行请求
        :param my_request: MyRequest对象请求
        :return: 响应
        """
        try:
            if my_request.need_proxy:
                proxy = self.proxy.get_proxy()
                if proxy:
                    proxies = {
                        'http': 'http://' + proxy,
                        'https': 'https://' + proxy
                    }
                    resp = requests.get(url=my_request.url, timeout=my_request.timeout, proxies=proxies,
                                        headers=my_request.headers)
                    return resp
            resp = requests.get(url=my_request.url, timeout=my_request.timeout, headers=my_request.headers)
            return resp
        except (ConnectionError, ReadTimeout) as e:
            print('ERROR:', e.args)
            return False
