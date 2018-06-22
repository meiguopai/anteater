# coding=utf-8

from testgroup.AutoTest.Lib.UtilityTools import *
from testgroup.AutoTest.Projects.TXCP.DB.OperateDB import truncate_data, load_data

sys.path.append(os.path.abspath(os.path.dirname(__file__) + os.path.sep + "../../../.."))

"""
说明：
    BaseParamSet：项目基础路径、测试用例目录等，仅需要修改CASE_XLSX_PATH->excel测试用例名称、测试地址ip、测试数据库信息
    AllTestParamSet:待测试脚本、测试主题、邮箱列表（可根据实际需要修改）、需初始化的数据库数据文件名/数据库表名
"""
BASE_DIR = '.'


class BaseParamSet:
    """基础设置"""
    def __init__(self):
        self.BASE_DIR = BASE_DIR
        # 定义测试文件查找的目录
        self.TEST_DIR = self.BASE_DIR + r'/TestCase/'
        # 测试用例、测试结果excel存放目录
        self.PLAN_DIR = self.BASE_DIR + '/TestPlan/'
        # 测试用例存放路径
        self.CASE_XLSX_PATH = self.PLAN_DIR + 'testcase_module.xls'
        # 测试地址
        self.web_address = 'http://192.168.142.172:8082'
        # 数据库地址
        self.host = '192.168.142.126'
        # 数据库用户名
        self.user = 'root'
        # 数据库密码
        self.password = 'password'
        # 数据库名
        self.dbname = 'txcp_db_business_test'


class AllTestParamSet:
    """all_test.py"""
    def __init__(self):
        # 指定测试脚本
        self.TEST_NUM = '0'
        # 测试主题
        self.TEST_SUBJECT = '**迭代五自动化测试报告'
        # 测试报告发送邮箱列表
        self.RECEIVER_LIST = ['a@***.com', 'b@***.com', 'c@***.com',
                              'd@***.com']
        self.table_list = ['t_offline_need', 't_offline_record', 't_tort_record']
        self.table_data_file = ['t_offline_need.sql', 't_offline_record.sql', 't_tort_record.sql']


if __name__ == "__main__":
    # 数据库测试数据准备
    truncate_data(AllTestParamSet().table_list)
    load_data(AllTestParamSet().table_data_file, './Data/')

    # 执行测试并发送邮件
    send_report(AllTestParamSet().RECEIVER_LIST, AllTestParamSet().TEST_SUBJECT,
                html_report(BASE_DIR, BaseParamSet().TEST_DIR, AllTestParamSet().TEST_NUM, AllTestParamSet().TEST_SUBJECT))
