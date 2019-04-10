import hashlib
import re

from pyquery import PyQuery as pq

from spider.config import BASE_URL
from spider.utils.myrequest import MyRequest


class Parser:

    def parse_index(self, response):
        """
        解析首页获取待请求的url
        :param response: 响应
        :return: 待请求url数据
        """
        # suffix
        exps = ['e_10{}/'.format(i) for i in range(2, 8)]
        pages = ['?page={}&ka=page-{}'.format(i, i) for i in range(1, 11)]
        suffixes = []
        for exp in exps:
            for p in pages:
                suffixes.append(exp + p)
        # parse
        doc = pq(response.text)
        menu = doc('#main .job-menu dl:first-child .menu-sub')
        subs = menu.items('a')
        for sub in subs:
            href = sub.attr('href')
            if not re.match('.*?99/$', href):
                for suffix in suffixes:
                    url = BASE_URL + href + suffix
                    yield MyRequest(url, self.parse_detail)

    def parse_detail(self, response):
        """
        解析招聘详情页面获得需要的信息
        :param response: 响应
        :return: 招聘数据
        """
        doc = pq(response.text)
        ul = doc('.job-list ul')
        if ul.length < 10:
            return None
        lis = ul.items('.job-primary')
        for li in lis:
            primary = li('.info-primary')
            primary_details = primary('p').html().split('<em class="vline"/>')
            company = li('.info-company .company-text')
            company_details = company('p').html().split('<em class="vline"/>')
            if len(primary_details) < 3 or len(company_details) < 3:
                continue
            data = {
                'job_title': primary('.name .job-title').text(),
                'wage': primary('.name .red').text(),
                'location': primary_details[0],
                'req_exp': primary_details[1],
                'req_degree': primary_details[2],
                'company': company('.name').text(),
                'industry': company_details[0],
                'stage': company_details[1],
                'scale': company_details[2]
            }
            md5 = hashlib.md5()
            for k, v in data.items():
                value = v.strip()
                data[k] = value
                md5.update(value.encode('utf-8'))
            data['id'] = md5.hexdigest()
            yield data
