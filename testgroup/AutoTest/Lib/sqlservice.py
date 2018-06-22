#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function
import pymysql
import psycopg2

class SqlService(object):
    def __init__(self, host, user, password, dbname=""):
        self.host = host
        self.user = user
        self.passwd = password
        self.dbname = dbname

    def conn(self):
        pass

    def setconn(self, conn, cur):
        self.conn = conn
        self.cur = cur

    def selectdb(self, dbname):
        self.conn.select_db(dbname)

    # insert, update, delete
    def execute(self, statement, params=()):
        self.cur = self.conn.cursor()
        if len(params) == 0:
            self.cur.execute(statement)
        else:
            self.cur.execute(statement, params)

        self.conn.commit()
        self.cur.close()

    # query
    def select(self, statement, params = ()):
        self.cur = self.conn.cursor()
        if len(params) == 0:
            self.cur.execute(statement)
        else:
            self.cur.execute(statement, params)
        results = self.cur.fetchall()

        self.cur.close()
        return results

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    # 批量的插入数据
    # 执行单条sql语句, 重复执行参数列表中参数
    def executemany(self, statement, params):
        if len(params) == 0:
            return
        else:
            self.cur = self.conn.cursor()
            self.cur.executemany(statement, params)

        self.conn.commit()
        self.cur.close()

    # 关闭connection连接
    def close(self):
        self.conn.close()

class MySqlService(SqlService):
    def __init__(self, host, user, password, dbname=""):
        super(MySqlService, self).__init__(host, user, password, dbname)

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.dbname, charset='utf8', use_unicode=True)
            self.cur = self.conn.cursor()
            super(MySqlService, self).setconn(self.conn, self.cur)
            return self.conn
        except pymysql.Error as e:
            print("connect {}  server, user: {} , passwd: {}, exception: {}, {}").format(self.host, self.user, self.passwd,
                   e.args[0], e.args[1])
            return None

class PgSqlService(SqlService):
    def __init__(self, host, user, password, dbname=""):
        super(PgSqlService, self).__init__(host, user, password, dbname)

    def connect(self):
        try:
            self.conn = psycopg2.connect(host=self.host, user=self.user, password=self.passwd, database=self.dbname, port="5432")
            self.cur = self.conn.cursor()
            super(PgSqlService, self).setconn(self.conn, self.cur)
            return self.conn
        except psycopg2.Error as e:
            print("connect {}  server, user: {} , passwd: {}, exception: {}, {}").format(self.host, self.user, self.passwd,
                   e.pgcode, e)
            return None
