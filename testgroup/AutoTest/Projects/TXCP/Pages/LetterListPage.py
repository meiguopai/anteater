#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:liuyaqing
import time
import os
from selenium.webdriver.common.by import By
from testgroup.AutoTest.Lib.BasePage import BasePage
from pykeyboard import PyKeyboard


class LetterList(BasePage):
    law_loc = (By.XPATH, "//span[contains(.,'法务管理')]")
    letterlist_loc = (By.XPATH, "//li[contains(.,'法务处理')]")
    query_loc = (By.XPATH, "//button[contains(.,'查询')]")
    export_loc = (By.XPATH, "//button[contains(.,'导出')]")
    import_loc = (By.XPATH, "//button[contains(.,'导入')]")
    letter_status_loc = (By.XPATH, "//input[@placeholder='法务处理状态']")
    stay_letter_loc = (By.XPATH, "//li[contains(.,'待发函')]")
    already_letter_loc = (By.XPATH, "//li[contains(.,'已发函')]")
    copyright_name_loc = (By.XPATH, "//input[@placeholder='版权名']")
    start_date_loc = (By.XPATH, "//input[@placeholder='开始日期']")
    end_date_loc = (By.XPATH, "//input[@placeholder='结束日期']")

    parent_path = os.path.abspath(os.path.dirname(__file__) + os.path.sep + "..")
    import_file_path = os.path.join(parent_path, 'Data\\already_letter_result.xls')

    # 打开法务管理菜单
    def open_law(self):
        self.find_element_by(*self.law_loc).click()

    # 打开法务处理菜单
    def open_letterlist(self):
        self.find_element_by(*self.letterlist_loc).click()

    # 导出待发函信息
    def export_letterlist(self):
        self.find_element_by(*self.export_loc).click()

    # 法务处理状态查询
    def query_by_letter_status(self):
        self.find_element_by(*self.letter_status_loc).click()
        # self.find_element_by(*self.stay_letter_loc).click()
        self.find_element_by(*self.already_letter_loc).click()

    # 版权名查询
    def query_by_copyright_name(self, copyrightname):
        self.find_element_by(*self.copyright_name_loc).send_keys(copyrightname)
        time.sleep(1)
        self.find_element_by(*self.query_loc).click()

    # 审核时间查询
    def query_by_date(self, startdate, enddate):
        self.find_element_by(*self.start_date_loc).send_keys(startdate)
        time.sleep(1)
        self.find_element_by(*self.end_date_loc).send_keys(enddate)
        time.sleep(1)
        self.find_element_by(*self.query_loc).click()

    # 导入已发函记录
    def import_letterlist(self):
        self.find_element_by(*self.letter_status_loc).click()
        self.find_element_by(*self.already_letter_loc).click()
        time.sleep(1)
        self.find_element_by(*self.import_loc).click()
        k = PyKeyboard()  # 定义一个实例
        time.sleep(1)
        k.tap_key(k.shift_key)  # 切换为英文
        time.sleep(1)
        k.type_string(self.import_file_path)  # 打开文件所在目录
        time.sleep(1)
        k.tap_key(k.enter_key)
        time.sleep(1)

    def page_value(self):
        return self.find_element_by(*(By.XPATH, "//span[@class='el-pagination__total']")).text


# 打开法务管理->法务处理标签页
def set_window(law):
    law.open_law()
    time.sleep(1)
    law.open_letterlist()
    time.sleep(1)
    return law
