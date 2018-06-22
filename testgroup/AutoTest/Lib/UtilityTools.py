#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import division
import requests
from itertools import product
from base.mail import SendEmail
import time
import unittest
from testgroup.AutoTest.Lib import HTMLTestRunner_PY3
from base.utils.log import *
from testgroup.AutoTest.Projects.BaseTest.Data.base_data import *

Logger().enableConsole(True)
log = Logger().getLogger('UtilityTools', './{}.log'.format('UtilityTools'))


def response_json_data(params, url, method, file_path=""):
    """
    发送请求，解析json, return data   author : panyuanyuan 20180522
    :param params: 请求所需的参数，字典的形式
    :param url: 目的地址
    :param method: 请求方法：GET、POST、FILE，错写或不填默认POST
    :param file_path: method为FILE时，需指定上传的文件路径
    :return:
    """
    requests.Session()
    if method == 'GET':
        response = requests.get(url=url, params=params, verify=False)
    elif method == 'FILE':
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url=url, params=params, verify=False, files=files)
    else:
        response = requests.post(url=url, params=params, verify=False)
    data = response.json()
    return data


def param_parse(datas, col_name):
    """
    根据参数个数生成需要传递的参数列表   author : panyuanyuan 20180522
    :param datas: 从excel表中读出的一条数据
    :param col_name: 需要处理的单元格所在列的名称
    :return:
    """
    # 表格数据转换成字典
    params_data = param_to_dict(datas, col_name)

    param_key_list = [param_key for param_key in params_data.keys()]
    param_value_list = [tuple(param_value) for param_value in params_data.values()]
    # itertools.product 计算笛卡尔积
    params_value = list(product(*param_value_list))

    # 将参数组合转换成对应的字典后以列表的形式返回
    params_list = []
    for param in params_value:
        params_dic = {}
        for param_count in range(len(param_key_list)):
            params_dic[param_key_list[param_count]] = param[param_count]
        params_list.append(params_dic)

    return params_list


def param_to_dict(datas, col_name):
    """
    表格数据转换成字典   author : panyuanyuan 20180522
    :param datas: 从excel表中读出的一条数据
    :param col_name: 需要处理的单元格所在列的名称
    :return:
    """
    params_data = {}
    for data in datas[col_name].split('\n'):
        key_value = data.split(':')
        params_data[key_value[0]] = eval(key_value[1].replace('{', '').replace('}', ''))
    return params_data


def html_report(base_dir, case_dir, case_num, case_subject):
    """
    执行测试：生成HTML报告
    :param base_dir:项目基础目录
    :param case_dir:测试用例目录
    :param case_num:测试用例文件名
    :param case_subject:测试主题
    :return:生成的报告路径
    """
    # 获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 指定生成报告存放目录
    report_dir = base_dir + r'/Report/'
    filename = report_dir + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner_PY3.HTMLTestRunner(
        stream=fp,
        title=case_subject,
        description=u'测试用例执行结果'
    )
    # 执行测试
    runner.run(creatsuite(case_dir, case_num))
    fp.close()
    return report_dir


def creatsuite(case_dir, case_num):
    """
    构造测试集：根据测试用例创建一个测试套件
    :param case_dir: 测试用例路径
    :param case_num: 测试用例文件名
    :return:
    """
    testunit = unittest.TestSuite()
    # discover标准加载测试用例并返回套件
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern='Test{}*.py'.format(str(case_num)),
                                                   top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    # 可以直接返回discover，下面主要用于调整测试用例的执行顺序
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit


def send_report(receiver_list, test_subject, report_path):
    """
    自动发送邮件
    :param receiver_list: 接收者列表
    :param test_subject: 邮件主题
    :param report_path: 附件路径
    :return:
    """
    send_email = SendEmail.Mail(user="liuxs@***.com", pwd="password", sender='liuxs@***.com',
                               receiver=receiver_list, subject=test_subject)
    new_report = send_email.new_report(report_path)
    send_email.send_file(new_report)
    log.info('send email success...')

if __name__ == '__main__':
    pass
