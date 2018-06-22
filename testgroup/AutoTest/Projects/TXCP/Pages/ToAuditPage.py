#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:liuyaqing
import time
from selenium.webdriver.common.by import By
from testgroup.AutoTest.Lib.BasePage import BasePage


class ToAudit(BasePage):
    tort_loc = (By.XPATH, "//span[contains(.,'侵权管理')]")
    website_to_audit_loc = (By.XPATH, "//i[@class='fa fa-check-square']")
    # 查询条件定位
    query_loc = (By.XPATH, "//button[contains(.,'查询')]")
    copyright_name_loc = (By.XPATH, "//input[@placeholder='版权名']")
    start_date_loc = (By.XPATH, "//input[@placeholder='开始日期']")
    end_date_loc = (By.XPATH, "//input[@placeholder='结束日期']")
    ss = (By.CSS_SELECTOR, "tr.el - table__row: nth - child(1) > td:nth - child(2) > div: nth - child(1)")
    # 审核清单
    audit_list_loc = (By.XPATH, "//button[contains(.,'审核清单')]")
    web_loc = (By.CSS_SELECTOR, "tr.el-table__row:nth-child(1) > td:nth-child(2) > div:nth-child(1)")
    # 页面条数定位
    query_cnt_loc = (By.CLASS_NAME, "el-pagination__total")

    # 打开侵权管理标签页
    def open_tort(self):
        self.find_element_by(*self.tort_loc).click()

    # 打开待审核网站列表标签页
    def open_toaudit(self):
        self.find_element_by(*self.website_to_audit_loc).click()

    # 版权名查询
    def query_by_copyright_name(self, copyrightname):
        self.find_element_by(*self.copyright_name_loc).send_keys(copyrightname)

    # 审核清单
    def audit_list(self):
        self.find_element_by(*self.audit_list_loc).click()

    # 入库时间查询
    def query_by_date(self, startdate, enddate):
        self.find_element_by(*self.start_date_loc).send_keys(startdate)
        self.find_element_by(*self.end_date_loc).send_keys(enddate)

    # 查询按钮
    def query_check(self):
        self.find_element_by(*self.query_loc).click()

    def get_website(self):
        website = self.find_element_by(*self.web_loc).text

        return website

    def query_cnt(self):
        query_cnt = self.find_element_by(*self.query_cnt_loc).text
        return int(query_cnt.strip(query_cnt[0]+query_cnt[-1]).strip())


# 打开侵权管理->待审核网站列表标签页
def set_window(toaudit):
    toaudit.open_tort()
    time.sleep(1)
    toaudit.open_toaudit()
    time.sleep(2)
    return toaudit
