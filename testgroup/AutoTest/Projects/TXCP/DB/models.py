#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : panyuanyuan 20180528

from __future__ import division

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, Index, Integer, JSON, SmallInteger, String, Table, Text, text, Date, Binary, LargeBinary
from sqlalchemy import ForeignKey, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# declare a Mapping,this is the class describe map to table column
Base = declarative_base()
metadata = Base.metadata
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


"""t_offline_need"""
def OfflineNeedItem(tablename):
    '''
        需要下线 表的定义
    '''
    class OfflineNeed(Base):
        __tablename__ = tablename

        id = Column('id', BigInteger, primary_key=True, autoincrement=True)
        origin_id = Column(BigInteger)  # 爬虫库的原始ID（无实际业务作用，便于研发回溯问题）
        website_id = Column(Integer)  # 网站ID（关联t_website表）
        belong_institution = Column(Integer)  # 归属机构（1：讯思雅；2：腾讯）
        catch_institution = Column(Integer)  # 发现机构（1：讯思雅；2：腾讯）
        copyright_name = Column(Text)  # 版权名（需保持跟版权库一致）
        video_name = Column(String(100))  # 视频实际名称（以资源原名为准）
        duration_sec = Column(String(400))  # 时长-秒（必填，默认0；在前端展示时切为分和秒）
        url_real = Column(String(1000))  # 真实地址/访问地址
        url_redirect = Column(String(1000))  # 跳转地址
        refer_source = Column(String(1000))  # 转载来源（微博）
        refer_user = Column(String(200))  # 转载来源用户名（微博）
        netdisk_md5 = Column(String(32))  # 网盘MD5
        netdisk_pwd = Column(String(20))  # 网盘密码
        netdisk_suk = Column(String(100))  # 网盘SUK
        upload_time = Column(DateTime)  # 上传时间
        upload_user = Column(String(200))  # 上传人
        tort_result = Column(Integer)  # 0：未侵权；1：侵权（默认）
        offline_status = Column(Integer)  # 0：未下线（默认）；1：已下线
        offline_need = Column(Integer)  # 0：不确定（延后处理，默认）；1：需下线
        offline_time = Column(DateTime)  # 下线时间
        enter_time = Column(DateTime)  # 入库时间
        audit_time = Column(DateTime)  # 审核时间（以下线审核时间为准）
        sync_status = Column(Integer)  # 同步到需下线清单表的状态 0：未同步（默认）；1：已同步
        status = Column(Integer)  # 0：初始入库状态（待侵权审核）；1：侵权审核完成（待下线审核）；2：下线审核完成（待下线操作）；3：下线操作完成（可由同步脚本同步到需下线清单表）

        copy_itemlist = ['origin_id', 'website_id', 'belong_institution', 'catch_institution', 'copyright_name',
                         'video_name', 'duration_sec', 'url_real', 'url_redirect', 'refer_source', 'refer_user',
                         'netdisk_md5', 'netdisk_pwd', 'netdisk_suk', 'upload_time', 'tort_result', 'offline_status',
                         'offline_need', 'offline_time', 'enter_time', 'audit_time', 'sync_status', 'status', ]

    return OfflineNeed

"""t_offline_record"""


def OfflineRecordItem(tablename):
    '''
        下线记录 表的定义
    '''
    class OfflineRecord(Base):
        __tablename__ = tablename

        id = Column('id', BigInteger, primary_key=True, autoincrement=True)
        origin_id = Column(BigInteger)  # 爬虫库的原始ID（无实际业务作用，便于研发回溯问题）
        website_id = Column(Integer)  # 网站ID（关联t_website表）
        belong_institution = Column(Integer)  # 归属机构（1：讯思雅；2：腾讯）
        catch_institution = Column(Integer)  # 发现机构（1：讯思雅；2：腾讯）
        copyright_name = Column(Text)  # 版权名（需保持跟版权库一致）
        video_name = Column(String(100))  # 视频实际名称（以资源原名为准）
        duration_sec = Column(String(400))  # 时长-秒（必填，默认0；在前端展示时切为分和秒）
        url_real = Column(String(1000))  # 真实地址/访问地址
        url_redirect = Column(String(1000))  # 跳转地址
        refer_source = Column(String(1000))  # 转载来源（微博）
        refer_user = Column(String(200))  # 转载来源用户名（微博）
        netdisk_md5 = Column(String(32))  # 网盘MD5
        netdisk_pwd = Column(String(20))  # 网盘密码
        netdisk_suk = Column(String(100))  # 网盘SUK
        upload_time = Column(DateTime)  # 上传时间
        upload_user = Column(String(200))  # 上传人
        tort_result = Column(Integer)  # 0：未侵权；1：侵权（默认）
        offline_status = Column(Integer)  # 0：未下线（默认）；1：已下线
        offline_need = Column(Integer)  # 0：不确定（延后处理，默认）；1：需下线
        offline_time = Column(DateTime)  # 下线时间
        enter_time = Column(DateTime)  # 入库时间
        audit_time = Column(DateTime)  # 审核时间（以下线审核时间为准）

        copy_itemlist = ['origin_id', 'website_id', 'belong_institution', 'catch_institution', 'copyright_name',
                         'video_name', 'duration_sec', 'url_real', 'url_redirect', 'refer_source', 'refer_user',
                         'netdisk_md5', 'netdisk_pwd', 'netdisk_suk', 'upload_time', 'tort_result', 'offline_status',
                         'offline_need', 'offline_time', 'enter_time', 'audit_time']

    return OfflineRecord

"""t_tort_record"""


def TortRecordItem(tablename):
    '''
        侵权清单 表的定义
    '''
    class TortRecord(Base):
        __tablename__ = tablename

        id = Column('id', BigInteger, primary_key=True, autoincrement=True)
        origin_id = Column(BigInteger)  # 爬虫库的原始ID（无实际业务作用，便于研发回溯问题）
        website_id = Column(Integer)  # 网站ID（关联t_website表）
        belong_institution = Column(Integer)  # 归属机构（1：讯思雅；2：腾讯）
        catch_institution = Column(Integer)  # 发现机构（1：讯思雅；2：腾讯）
        copyright_name = Column(Text)  # 版权名（需保持跟版权库一致）
        video_name = Column(String(100))  # 视频实际名称（以资源原名为准）
        duration_sec = Column(String(400))  # 时长-秒（必填，默认0；在前端展示时切为分和秒）
        url_real = Column(String(1000))  # 真实地址/访问地址
        url_redirect = Column(String(1000))  # 跳转地址
        refer_source = Column(String(1000))  # 转载来源（微博）
        refer_user = Column(String(200))  # 转载来源用户名（微博）
        netdisk_md5 = Column(String(32))  # 网盘MD5
        netdisk_pwd = Column(String(20))  # 网盘密码
        netdisk_suk = Column(String(100))  # 网盘SUK
        upload_time = Column(DateTime)  # 上传时间
        upload_user = Column(String(200))  # 上传人
        tort_result = Column(Integer)  # 0：未侵权；1：侵权（默认）
        offline_status = Column(Integer)  # 0：未下线（默认）；1：已下线
        offline_need = Column(Integer)  # 0：不确定（延后处理，默认）；1：需下线
        offline_time = Column(DateTime)  # 下线时间
        enter_time = Column(DateTime)  # 入库时间
        audit_time = Column(DateTime)  # 审核时间（以下线审核时间为准）
        sync_status = Column(Integer)  # 同步到需下线清单表的状态 0：未同步（默认）；1：已同步
        status = Column(Integer)  # 0：初始入库状态（待侵权审核）；1：侵权审核完成（待下线审核）；2：下线审核完成（待下线操作）；3：下线操作完成（可由同步脚本同步到需下线清单表）

        copy_itemlist = ['origin_id', 'website_id', 'belong_institution', 'catch_institution', 'copyright_name',
                         'video_name', 'duration_sec', 'url_real', 'url_redirect', 'refer_source', 'refer_user',
                         'netdisk_md5', 'netdisk_pwd', 'netdisk_suk', 'upload_time', 'tort_result', 'offline_status',
                         'offline_need', 'offline_time', 'enter_time', 'audit_time', 'sync_status', 'status']

    return TortRecord

"""t_website"""


def WebsiteItem(tablename):
    '''
        网站定义 表的定义
    '''
    class WebsiteRecord(Base):
        __tablename__ = tablename

        id = Column('id', Integer, primary_key=True, autoincrement=True)
        name = Column(String(100))  # 网站名（中文名称；需人工维护准确性）
        url = Column(String(1000))  # 网站入口地址
        category = Column(String(100))  # 所属数据来源类型
        platform = Column(Integer)  # 所属平台类型
        query_times = Column(Integer)  # 查询次数，作为前端网站下拉列表排序字段
        status = Column(Integer)  # -1：已删除；1：在用
        enter_time = Column(DateTime)  # 入库时间

        copy_itemlist = ['name', 'url', 'category', 'platform', 'query_times', 'status', 'enter_time']

    return WebsiteRecord


def map_item(item, sql_item):
    """ 将数据项从 map_item 拷贝到 sqlalchemy_item """

    for key in item.keys():
        sql_item.__setattr__(key, item[key])
    return sql_item


def create_session(url, echo=True):
    # declare the connecting to the server
    engine = create_engine(url, encoding='utf-8', echo=echo)
    # connect session to active the action
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == '__main__':
    pass
