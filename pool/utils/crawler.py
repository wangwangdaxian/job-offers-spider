from pool.utils import request


class Crawler(object):
    def __init__(self):
        count = 0
        self.__CrawlFunc__ = []
        for method in dir(self):
            if 'crawl_' in method:
                self.__CrawlFunc__.append(method)
                count += 1
        self.__CrawFuncCount__ = count

    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    # def crawl_kuaidaili(self, page_count=2):
    #     """
    #     获取快代理的免费代理
    #     :return: 代理
    #     """
    #     start_url = 'https://www.kuaidaili.com/free/inha/{}/'
    #     urls = [start_url.format(page) for page in range(1, page_count + 1)]
    #     for url in urls:
    #         time.sleep(3)
    #         print('Crawling', url)
    #         html = request.get_page(url)
    #         if html:
    #             doc = pq(html.text)
    #             trs = doc('#list table tr:gt(0)').items()
    #             for tr in trs:
    #                 ip = tr('td[data-title="IP"]').text()
    #                 port = tr('td[data-title="PORT"]').text()
    #                 yield ':'.join([ip, port])
    #
    # def crawl_xici(self, page_count=2):
    #     """
    #     获取西刺代理的免费代理
    #     :return: 代理
    #     """
    #     start_url = 'https://www.xicidaili.com/nn/{}'
    #     urls = [start_url.format(page) for page in range(1, page_count + 1)]
    #     for url in urls:
    #         time.sleep(3)
    #         print('Crawling', url)
    #         html = request.get_page(url)
    #         if html:
    #             doc = pq(html.text)
    #             trs = doc('#ip_list tr:gt(1)').items()
    #             for tr in trs:
    #                 ip = tr('td:nth-child(2)').text()
    #                 port = tr('td:nth-child(3)').text()
    #                 yield ':'.join([ip, port])
    #
    # def crawl_qingting(self):
    #     """
    #     获取蜻蜓代理的免费代理
    #     :return: 代理
    #     """
    #     start_url = 'http://proxy.horocn.com/api/free-proxy?app_id={}&format=text'
    #     app_id = '163016700225102919402'
    #     url = start_url.format(app_id)
    #     print('Crawling', url)
    #     html = request.get_page(url)
    #     proxies = html.text.split('\n')
    #     for proxy in proxies:
    #         yield proxy
    #
    # def crawl_ashtwo(self):
    #     """
    #     获取ashtwo的免费代理
    #     :return: 代理
    #     """
    #     start_url = 'http://p.ashtwo.cn/'
    #     print('Crawling', start_url)
    #     proxies = []
    #     for i in range(0, 20):
    #         time.sleep(0.5)
    #         html = request.get_page(start_url)
    #         doc = pq(html.text)
    #         proxy = doc('body p').text()
    #         proxies.append(proxy)
    #     for proxy in proxies:
    #         yield proxy
    #
    # def crawl_wuyou(self):
    #     """
    #     获取无忧代理的免费代理
    #     :return: 代理
    #     """
    #     start_url = 'http://www.data5u.com/free/{}/index.shtml'
    #     types = ['gngn', 'gwgn']
    #     urls = [start_url.format(tp) for tp in types]
    #     for url in urls:
    #         time.sleep(1)
    #         print('Crawling', url)
    #         html = request.get_page(url)
    #         if html:
    #             doc = pq(html.text)
    #             uls = doc('.wlist .l2').items()
    #             for ul in uls:
    #                 ip = ul('span:first-child li:first-child').text()
    #                 port = ul('.port').text()
    #                 yield ':'.join([ip, port])

    def crawl_qt(self):
        """
        获取蜻蜓代理的私密代理
        :return: 代理
        """
        url = 'https://proxy.horocn.com/api/proxies?order_id=HXOH1630506293222425&num=10&format=text'
        print('Crawling', url)
        html = request.get_page(url)
        proxies = html.text.split('\n')
        for proxy in proxies:
            yield proxy
