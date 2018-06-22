#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:panyuanyuan
import time
from selenium.webdriver.common.by import By
from testgroup.AutoTest.Lib.BasePage import BasePage


class ReportExport(BasePage):
    report_loc = (By.XPATH, "//span[contains(.,'统计报告')]")
    report_export_loc = (By.XPATH, "//i[@class='fa fa-table']")
    export_loc = (By.XPATH, "//span[contains(.,'生成报告')]")
    start_date_loc = (By.XPATH, "//input[@placeholder='开始日期']")
    end_date_loc = (By.XPATH, "//input[@placeholder='结束日期']")

    # 打开统计报告菜单
    def open_report(self):
        self.find_element_by(*self.report_loc).click()

    # 打开报表导出菜单
    def open_report_export(self):
        self.find_element_by(*self.report_export_loc).click()

    # 导出时间选择
    def export_by_date(self, startdate, enddate):
        self.find_element_by(*self.start_date_loc).send_keys(startdate)
        self.find_element_by(*self.end_date_loc).send_keys(enddate)
        self.find_element_by(*self.export_loc).click()
        time.sleep(15)

    def page_value(self):
        return self.find_element_by(*(By.XPATH, "//span[@class='el-pagination__total']")).text


# 打开法务管理->法务处理标签页
def set_window(report):
    report.open_report()
    time.sleep(1)
    report.open_report_export()
    time.sleep(1)
    return report
