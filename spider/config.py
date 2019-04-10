# 代理配置
PROXY_POOL_URL = 'http://127.0.0.1:5000/random'

# 待爬取网站配置
INDEX_URL = 'https://www.zhipin.com/?city=c101020100'
BASE_URL = 'https://www.zhipin.com'

# Redis数据库配置
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
REDIS_PASSWORD = 'reggie'
REDIS_KEY = 'zhiping'

# Mysql数据库配置
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = '3306'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DATABASE = 'spider'

MYSQL_TABLE = 'job_offers'
MYSQL_SCHEMA = 'job_title VARCHAR(255),wage VARCHAR(255),location VARCHAR(255),req_exp VARCHAR(255),req_degree ' \
               'VARCHAR(255),company VARCHAR(255),industry VARCHAR(255),stage VARCHAR(255),scale VARCHAR(255),' \
               'id CHAR(32) '
