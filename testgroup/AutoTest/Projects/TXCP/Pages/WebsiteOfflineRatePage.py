#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:panyuanyuan
import time
from selenium.webdriver.common.by import By
from testgroup.AutoTest.Lib.BasePage import BasePage


class WebsiteOfflineRate(BasePage):
    report_loc = (By.XPATH, "//span[contains(.,'统计报告')]")
    report_export_loc = (By.XPATH, "//li[4]/ul/li[3]")
    query_loc = (By.XPATH, "//span[contains(.,'查询')]")
    start_date_loc = (By.XPATH, "//input[@placeholder='开始时间']")
    end_date_loc = (By.XPATH, "//input[@placeholder='截止时间']")
    webiste_loc = (By.CSS_SELECTOR, "input.el-input__inner")
    bibi_loc = (By.XPATH, "//span[contains(.,'哔哩哔哩')]")

    first_webiste_name_loc = (By.XPATH, "//tr[@class='el-table__row'][1]/td[2]/div")

    # 打开统计报告菜单
    def open_report(self):
        self.find_element_by(*self.report_loc).click()

    # 打开报表导出菜单
    def open_report_export(self):
        self.find_element_by(*self.report_export_loc).click()

    # 获取第一条数据的网站名称
    def get_first_website_name(self):
        return self.find_element_by(*self.first_webiste_name_loc).text

    # 网站列表查询
    def query_by_website(self):
        self.find_element_by(*self.webiste_loc).click()
        self.find_element_by(*self.bibi_loc).click()

    # 审核时间查询
    def query_by_date(self, startdate, enddate):
        self.find_element_by(*self.start_date_loc).send_keys(startdate)
        self.find_element_by(*self.end_date_loc).send_keys(enddate)
        self.find_element_by(*self.query_loc).click()

    def page_value(self):
        return self.find_element_by(*(By.XPATH, "//span[@class='el-pagination__total']")).text


# 打开统计报告->网站下线率统计标签页
def set_window(report):
    report.open_report()
    time.sleep(1)
    report.open_report_export()
    time.sleep(1)
    return report
