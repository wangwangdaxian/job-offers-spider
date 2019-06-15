# Job Offer Spider
job-offer-spider是一个爬虫学习项目，主要采用`requests`发起请求和`pyquery`解析页面。

本项目参考崔庆才的《Python3网络爬虫开发实战》一书编写。

项目设计上分为两个子模块，分别是代理池模块`pool`和爬虫模块`spider`。

## 代理池模块
代理池模块主要用作代理节点信息的抓取、测试和API接口服务，由`schedule`调度。

1. `getter.py`负责从第三方服务抓取代理节点信息，其调用的`Crawler`类下所有以‘crawl_’开头的方法会被顺序执行。

2. `db.py`负责将抓取到的代理节点信息存入Redis

3. `tester.py`负责测试存在Redis中的代理节点，多次测试失败时会删除失败的节点信息

4. `api.py`负责暴露API服务给爬虫模块，随机获取Redis中分数最高的节点信息返回

## 爬虫模块
爬虫模块主要抓取并解析BOSS直聘网站的招聘岗位信息，由`schedule`调度。

1. `myproxy.py`从代理池API服务中获取代理节点

2. `getter.py`执行请求

3. `parser.py`解析请求

## 运行使用
需要先更改代理池模块下`crawler.py`中的代理抓取方法为可用方法，并在环境中配置好Redis和MySQL数据库。

然后运行代理池模块的`scheduler`脚本，等待几分钟，使代理池采集足够的代理节点。

再运行爬虫模块的`schedule`脚本，等待爬虫运行完毕即可。