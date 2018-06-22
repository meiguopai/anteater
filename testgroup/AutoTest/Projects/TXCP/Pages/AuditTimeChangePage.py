#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:panyuanyuan
import time
import os
from selenium.webdriver.common.by import By
from testgroup.AutoTest.Lib.BasePage import BasePage


class AuditTime(BasePage):
    tort_loc = (By.XPATH, "//span[contains(.,'侵权管理')]")
    audit_time_change_loc = (By.XPATH, "//i[@class='fa fa-plus']")

    website_list_loc = (By.XPATH, "//div[contains(.,'网站列表')]//input[@placeholder='请选择']")
    bilibili_loc = (By.XPATH, "//li/span[contains(.,'哔哩哔哩')]")

    offline_all_loc = (By.XPATH, "//input[@placeholder='下线状态']")
    offline_select_loc = (By.XPATH, "//li[contains(.,'已下线')]")

    copyright_name_loc = (By.XPATH, "//input[@placeholder='版权名']")

    select_record_loc = (By.XPATH, "(//span[@class='el-checkbox__inner'])[2]")
    time_loc = (By.CSS_SELECTOR, "tr.el-table__row:nth-child(1) > td:nth-child(10) > div:nth-child(1) > span:nth-child(1)")

    data_source_loc = (By.XPATH, "//input[@placeholder='数据来源']")
    data_source_select_loc = (By.XPATH, "//li[contains(.,'非腾讯')]")

    query_loc = (By.XPATH, "//button[contains(.,'查询')]")
    confirm_loc = (By.XPATH, "//button[contains(.,'确认延后')]")

    # 页面条数定位
    query_cnt_loc = (By.CLASS_NAME, "el-pagination__total")

    # 下线审核
    offline_review_loc = (By.XPATH, "//button[contains(.,'下线操作')]")
    # 未下线
    not_offline_loc = (By.XPATH, "//button[contains(.,'未下线')]")

    # 打开侵权管理标签页
    def open_tort(self):
        self.find_element_by(*self.tort_loc).click()

    # 打开审核时间变更标签页
    def open_offline(self):
        self.find_element_by(*self.audit_time_change_loc).click()

    # 网站列表查询
    def query_by_website_list(self):
        self.find_element_by(*self.website_list_loc).click()
        time.sleep(1)
        self.find_element_by(*self.bilibili_loc).click()

    # 下线状态查询
    def query_by_offline_status(self):
        self.find_element_by(*self.offline_all_loc).click()
        time.sleep(1)
        self.find_element_by(*self.offline_select_loc).click()

    # 数据来源查询
    def query_by_data_source(self):
        self.find_element_by(*self.data_source_loc).click()
        time.sleep(1)
        self.find_element_by(*self.data_source_select_loc).click()

    # 版权名查询
    def query_by_copyright_name(self, copyright_name):
        self.find_element_by(*self.copyright_name_loc).send_keys(copyright_name)
        time.sleep(1)
        self.find_element_by(*self.query_loc).click()

    # 延后审核时间
    def audit_time_change(self):
        old_cnt = self.find_element_by(*self.time_loc).text
        self.find_element_by(*self.select_record_loc).click()
        time.sleep(1)
        self.find_element_by(*self.confirm_loc).click()
        time.sleep(1)
        new_cnt = self.find_element_by(*self.time_loc).text
        return old_cnt, new_cnt

    def page_value(self):
        return self.find_element_by(*(By.XPATH, "//span[@class='el-pagination__total']")).text

    def query_cnt(self):
        query_cnt = self.find_element_by(*self.query_cnt_loc).text
        return int(query_cnt.strip(query_cnt[0]+query_cnt[-1]).strip())


# 侵权管理->审核时间变更标签页
def set_window(offline):
    offline.open_tort()
    time.sleep(1)
    offline.open_offline()
    time.sleep(1)
    return offline

if __name__ == '__main__':
    print(os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + "."))
    print(os.path.abspath(os.path.dirname(__file__) + os.path.sep + ".."))
