#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:panyuanyuan
import time
from selenium.webdriver.common.by import By
from testgroup.AutoTest.Lib.BasePage import BasePage


class Wordload(BasePage):
    report_loc = (By.XPATH, "//span[contains(.,'统计报告')]")
    report_export_loc = (By.XPATH, "//i[@class='fa fa-folder-open']")

    qinquan_start_date_loc = (By.XPATH, "//div[@id='pane-qinquanData']//input[@placeholder='开始时间']")
    qinquan_end_date_loc = (By.XPATH, "//div[@id='pane-qinquanData']//input[@placeholder='截止时间']")
    qinquan_query_loc = (By.XPATH, "//div[@id='pane-qinquanData']//span[contains(.,'查询')]")
    qinquan_page_count_loc = (By.XPATH, "//div[@id='pane-qinquanData']//span[@class='el-pagination__total']")

    offline_start_date_loc = (By.XPATH, "//div[@id='pane-offlineData']//input[@placeholder='开始时间']")
    offline_end_date_loc = (By.XPATH, "//div[@id='pane-offlineData']//input[@placeholder='截止时间']")
    offline_query_loc = (By.XPATH, "//div[@id='pane-offlineData']//span[contains(.,'查询')]")
    offline_page_count_loc = (By.XPATH, "//div[@id='pane-offlineData']//span[@class='el-pagination__total']")

    lawLetter_start_date_loc = (By.XPATH, "//div[@id='pane-lawLetterData']//input[@placeholder='开始时间']")
    lawLetter_end_date_loc = (By.XPATH, "//div[@id='pane-lawLetterData']//input[@placeholder='截止时间']")
    lawLetter_query_loc = (By.XPATH, "//div[@id='pane-lawLetterData']//span[contains(.,'查询')]")
    lawLetter_page_count_loc = (By.XPATH, "//div[@id='pane-lawLetterData']//span[@class='el-pagination__total']")

    qinquanData_loc = (By.XPATH, "//div[@id='tab-qinquanData']")
    offlineData_loc = (By.XPATH, "//div[@id='tab-offlineData']")
    lawLetterData_loc = (By.XPATH, "//div[@id='tab-lawLetterData']")

    # 打开统计报告菜单
    def open_report(self):
        self.find_element_by(*self.report_loc).click()

    # 打开报表导出菜单
    def open_workload(self):
        self.find_element_by(*self.report_export_loc).click()

    # 打开侵权数据审核统计
    def open_qinquan_data(self, startdate, enddate):
        self.find_element_by(*self.qinquanData_loc).click()
        self.export_by_date(startdate, enddate, self.qinquan_start_date_loc, self.qinquan_end_date_loc,
                            self.qinquan_query_loc)

    # 打开下线审核数据统计
    def open_offline_data(self, startdate, enddate):
        self.find_element_by(*self.offlineData_loc).click()
        self.export_by_date(startdate, enddate, self.offline_start_date_loc, self.offline_end_date_loc,
                            self.offline_query_loc)

    # 打开法务发函数据统计
    def open_lawletter_data(self, startdate, enddate):
        self.find_element_by(*self.lawLetterData_loc).click()
        self.export_by_date(startdate, enddate, self.lawLetter_start_date_loc, self.lawLetter_end_date_loc,
                            self.lawLetter_query_loc)

    # 导出时间选择
    def export_by_date(self, startdate, enddate, start_date_loc, end_date_loc, query_loc):
        start = self.find_element_by(*start_date_loc)
        start.clear()
        start.send_keys(startdate)
        end = self.find_element_by(*end_date_loc)
        end.clear()
        end.send_keys(enddate)
        self.find_element_by(*query_loc).click()

    def qinquan_page_value(self):
        return self.find_element_by(*self.qinquan_page_count_loc).text

    def offline_page_value(self):
        return self.find_element_by(*self.offline_page_count_loc).text

    def lawletter_page_value(self):
        return self.find_element_by(*self.lawLetter_page_count_loc).text


# 打开法务管理->法务处理标签页
def set_window(report):
    report.open_report()
    time.sleep(1)
    report.open_workload()
    time.sleep(1)
    return report
