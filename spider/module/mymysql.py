import pymysql

from spider.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE, MYSQL_TABLE, MYSQL_SCHEMA


class MySQL:
    def __init__(self, host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT,
                 database=MYSQL_DATABASE):
        """
        MySQL初始化
        :param host:
        :param username:
        :param password:
        :param port:
        :param database:
        """
        try:
            self.db = pymysql.connect(host, username, password, database, charset='utf8', port=port)
            self.cursor = self.db.cursor()
            self.create()
        except pymysql.MySQLError as e:
            print(e.args)

    def insert(self, data, table=MYSQL_TABLE):
        """
        插入数据
        :param table:
        :param data:
        :return:
        """
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql_query = 'insert into %s (%s) values (%s)' % (table, keys, values)
        try:
            self.cursor.execute(sql_query, tuple(data.values()))
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()

    def create(self, schema=MYSQL_SCHEMA, table=MYSQL_TABLE):
        sql_query = 'create table if not exists %s (%s) DEFAULT CHARSET=utf8 ' % (table, schema)
        try:
            self.cursor.execute(sql_query)
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()
