#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:liuyaqing
import time
import os
from pykeyboard import PyKeyboard
from selenium.webdriver.common.by import By
from testgroup.AutoTest.Lib.BasePage import BasePage


class Offline(BasePage):
    tort_loc = (By.XPATH, "//span[contains(.,'侵权管理')]")
    offline_loc = (By.XPATH, "//div[@id='app']/section/section/div/ul/li[2]/ul/li[4]")
    import_offline_report_loc = (By.XPATH, "//button[contains(.,'腾讯下线清单导入')]")
    import_offline_result_loc = (By.XPATH, "//button[contains(.,'下线审核结果导入')]")
    website_list_loc = (By.XPATH, "//div[contains(.,'网站列表')]//input[@placeholder='请选择']")
    jrtt_loc = (By.XPATH, "//li/span[contains(.,'今日头条')]")
    letter_status_loc = (By.CSS_SELECTOR, "div.el-form-item:nth-child(2) > div:nth-child(1)")
    stay_letter_loc = (By.XPATH, "//li/span[contains(.,'未处理')]")
    url_loc = (By.XPATH, "//input[@placeholder='URL']")
    copyright_name_loc = (By.XPATH, "//input[@placeholder='版权名']")
    start_date_loc = (By.XPATH, "//input[@placeholder='开始日期']")
    end_date_loc = (By.XPATH, "//input[@placeholder='结束日期']")

    query_loc = (By.XPATH, "//button[contains(.,'查询')]")

    parent_path = os.path.abspath(os.path.dirname(__file__) + os.path.sep + "..")
    tx_offline_file_path = os.path.join(parent_path, 'Data\\tx_offline.xls')
    offline_result_file_path = os.path.join(parent_path, 'Data\\offline_result.xls')

    # 页面条数定位
    query_cnt_loc = (By.CLASS_NAME, "el-pagination__total")

    # 下线审核
    offline_review_loc = (By.XPATH, "//button[contains(.,'下线操作')]")
    # 未下线
    # not_offline_loc = (By.XPATH, "//button[contains(.,'未下线')]")
    not_offline_loc = (By.CSS_SELECTOR, "tr.el-table__row:nth-child(3) > td:nth-child(10) > div:nth-child(1) > button:nth-child(1)")

    # 打开侵权管理标签页
    def open_tort(self):
        self.find_element_by(*self.tort_loc).click()

    # 打开下线管理标签页
    def open_offline(self):
        self.find_element_by(*self.offline_loc).click()

    # 网站列表查询
    def query_by_website_list(self):
        self.find_element_by(*self.website_list_loc).click()
        time.sleep(1)
        self.find_element_by(*self.jrtt_loc).click()
        time.sleep(1)
        self.find_element_by(*self.query_loc).click()

    # 法务处理状态查询
    def query_by_letter_status(self):
        self.find_element_by(*self.letter_status_loc).click()
        time.sleep(1)
        self.find_element_by(*self.stay_letter_loc).click()
        time.sleep(1)
        self.find_element_by(*self.query_loc).click()

    # url查询
    def query_by_url(self, url):
        self.find_element_by(*self.url_loc).send_keys(url)
        self.find_element_by(*self.query_loc).click()

    # 版权名查询
    def query_by_copyright_name(self, copyright_name):
        self.find_element_by(*self.copyright_name_loc).send_keys(copyright_name)
        time.sleep(1)
        self.find_element_by(*self.query_loc).click()

    # 审核时间查询
    def query_by_date(self, start_date, end_date):
        self.find_element_by(*self.start_date_loc).send_keys(start_date)
        self.find_element_by(*self.end_date_loc).send_keys(end_date)
        time.sleep(1)
        self.find_element_by(*self.query_loc).click()

    # 腾讯下线清单导入
    def open_import_offline_report(self):
        k = PyKeyboard()  # 定义一个实例
        self.find_element_by(*self.import_offline_report_loc).click()  # 打开上传文件位置
        time.sleep(2)
        k.tap_key(k.shift_key)  # 切换为英文
        time.sleep(2)
        k.type_string(self.tx_offline_file_path)  # 打开文件所在目录
        time.sleep(2)
        k.tap_key(k.enter_key)

    # 下线审核结果导入
    def open_import_offline_result(self):
        k = PyKeyboard()
        self.find_element_by(*self.import_offline_result_loc).click()
        time.sleep(2)
        k.tap_key(k.shift_key)  # 切换为英文
        time.sleep(2)
        k.type_string(self.offline_result_file_path)  # 打开文件所在目录
        time.sleep(2)
        k.tap_key(k.enter_key)

    def page_value(self):
        return self.find_element_by(*(By.XPATH, "//span[@class='el-pagination__total']")).text

    def offline_review(self):
        self.find_element_by(*self.offline_review_loc).click()
        k = PyKeyboard()
        k.tap_key(k.enter_key)

    def not_offline(self):
        self.find_element_by(*self.not_offline_loc).click()

    def query_cnt(self):
        query_cnt = self.find_element_by(*self.query_cnt_loc).text
        return int(query_cnt.strip(query_cnt[0]+query_cnt[-1]).strip())


# 侵权管理->下线管理标签页
def set_window(offline):
    offline.open_tort()
    time.sleep(1)
    offline.open_offline()
    time.sleep(1)
    return offline

if __name__ == '__main__':
    print(os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + "."))
    print(os.path.abspath(os.path.dirname(__file__) + os.path.sep + ".."))
