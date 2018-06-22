#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : panyuanyuan

from __future__ import division
from testgroup.AutoTest.Projects.TXCP.DB import models
from testgroup.AutoTest.Lib.sqlservice import *
from base.utils.log import *

Logger().enableConsole(True)
log = Logger().getLogger('operateDB', './{}.log'.format('operateDB'))


class OperateDB:
    def __init__(self):
        self.Session = models.create_session('mysql+pymysql://root:Smart123@192.168.142.126:3306/txcp_db_business_test?charset=utf-8',
                                                    echo=False)
        self.OfflineNeedItem = models.OfflineNeedItem('t_offline_need')
        self.OfflineRecordItem = models.OfflineRecordItem('t_offline_record')
        self.TortRecordItem = models.TortRecordItem('t_tort_record')
        self.WebsiteItem = models.WebsiteItem('t_website')

    # 表内所有记录
    def select(self):
        itemquerys = self.Session.query(self.OfflineNeedItem).all()
        return itemquerys

    # 直接执行sql语句
    def execute_sql(self, sql):
        itemquerys = self.Session.execute(sql)
        return itemquerys

    # 查询：目的表，条件字段，条件值
    def query(self, table, value):
        if table == 't_offline_need':
            itemquerys = self.Session.query(self.OfflineNeedItem).filter(self.OfflineNeedItem.url_real == value).all()
        elif table == 't_offline_record':
            itemquerys = self.Session.query(self.OfflineRecordItem).filter(self.OfflineRecordItem.url_real == value).all()
        elif table == 't_tort_record':
            itemquerys = self.Session.query(self.TortRecordItem).filter(self.TortRecordItem.url_real == value).all()
        else:
            itemquerys = None
        return itemquerys

    # 删除
    def delete(self, instance):
        if instance is not None:
            if type(instance) == list:
                for i in instance:
                    self.Session.delete(i)
            else:
                self.Session.delete(instance)
        else:
            log.info('instance is None,please check it.')

    # 提交
    def commit(self):
        self.Session.commit()

    # 关闭连接
    def close(self):
        self.Session.close()


def mysql_execute(sql):
    db_conn = MySqlService(host="192.168.142.114", user="root", password="Smart123", dbname="txcp_db_business_test")
    con = db_conn.connect()
    if con:
        res = db_conn.select(statement=sql)
        db_conn.commit()
        return res
    else:
        log.info('connect error')
        return None


def load_data(infohash_file_name_list, infohash_file_path):
    """ 加载数据 """
    for infohash_file_name in infohash_file_name_list:
        with open(infohash_file_path + infohash_file_name, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                mysql_execute(line)
        log.info('file [{}]:load data success!'.format(infohash_file_name))
    log.info('load data over!')


def truncate_data(table_name_list):
    """ 清空表中数据 """
    for table_name in table_name_list:
        mysql_execute('TRUNCATE TABLE {}'.format(table_name))
        log.info('table [{}]:truncate data success!'.format(table_name))
    log.info('truncate data over!')


if __name__ == '__main__':
    # operate_db = OperateDB()
    # # # 清空表
    # # operate_db.delete(operate_db.select())
    # # operate_db.commit()
    # # # 插入记录
    # #
    # # with open('../Data/t_offline_need.sql', 'r+', encoding='utf-8') as f:
    # #     for line in f.readlines():
    # #         print(line)
    # #         operate_db.execute_sql(line)
    #
    # operate_db.execute_sql("")
    # operate_db.commit()
    # operate_db.close()

    # test load_data、truncate_data
    load_data(['t_offline_need.sql'], '../Data/')
    # truncate_data(['t_offline_need'])
    # test end
