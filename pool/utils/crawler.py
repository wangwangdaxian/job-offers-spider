import time

import requests
from pyquery import PyQuery as pq


class ProxyMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(mcs, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crwal_kuaidaili(self, page_count=10):
        """
        获取快代理
        :return: 代理
        """
        start_url = 'https://www.kuaidaili.com/free/inha/{}/'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            time.sleep(2)
            print('Crawling', url)
            html = requests.get(url)
            if html:
                doc = pq(html.text)
                trs = doc('#list table tr:gt(0)').items()
                for tr in trs:
                    ip = tr('td[data-title="IP"]').text()
                    port = tr('td[data-title="PORT"]').text()
                    yield ':'.join([ip, port])
