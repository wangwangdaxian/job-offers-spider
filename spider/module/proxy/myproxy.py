import requests

from spider.config import PROXY_POOL_URL


class MyProxy:

    def get_proxy(self):
        """
        从代理池获取代理
        :return: 代理
        """
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                print('Get Proxy From Pool', response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None
