#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:liuyaqing
import time
from selenium.webdriver.common.by import By
from testgroup.AutoTest.Lib.BasePage import BasePage


class TortAudit(BasePage):
    tort_loc = (By.XPATH, "//span[contains(.,'侵权管理')]")
    tort_audit_loc = (By.XPATH, "//li[contains(.,'待审核数据清单')]")
    # 查询条件定位
    query_loc = (By.XPATH, "//button[contains(.,'查询')]")
    webiste_loc = (By.CSS_SELECTOR, "input.el-input__inner")
    bibi_loc = (By.XPATH, "//span[contains(.,'哔哩哔哩')]")
    url_loc = (By.XPATH, "//input[@placeholder='URL']")
    copyright_name_loc = (By.XPATH, "//input[@placeholder='版权名']")
    startdate_loc = (By.XPATH, "//input[@placeholder='开始日期']")
    enddate_loc = (By.XPATH, "//input[@placeholder='结束日期']")
    # 审核登记
    audit_loc = (By.XPATH, "//button[contains(.,'审核登记')]")
    web_loc = (By.XPATH, "(//input[@type='text'])[7]")
    url_real_loc = (By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/div[4]/div/div[2]/form/div[6]/div/div/input')
    upload_time_loc = (By.XPATH, "//input[@placeholder='选择日期时间']")
    upload_user_loc = (By.XPATH, "(//input[@type='text'])[15]")
    # already_tort_loc = (By.XPATH, "//span[contains(.,'侵权')]")
    already_tort_loc = (By.CSS_SELECTOR, "div.el-form-item:nth-child(12) > div:nth-child(2) > div:nth-child(1) > label:nth-child(2) > span:nth-child(2)")
    need_offline_loc = (By.XPATH, "//span[contains(.,'需下线')]")
    confirm_loc = (By.XPATH, "//span[contains(.,'确 定')]")
    # 页面条数定位
    query_cnt_loc = (By.CLASS_NAME, "el-pagination__total")

    # 已下线元素定位
    offline_loc = (By.XPATH, "//button[contains(.,'已下线')]")
    website_loc = (By.XPATH, "//tr[@class='el-table__row'][1]/td[@class='el-table_3_column_18 is-left']/div")
    offline_url_loc = (By.XPATH, "//tr[@class='el-table__row'][1]/td[@class='el-table_3_column_21 is-left']/div/a")

    # 打开待审核数据清单标签页
    def open_tort_audit(self):
        self.find_element_by(*self.tort_loc).click()
        time.sleep(1)
        self.find_element_by(*self.tort_audit_loc).click()

    # 网站列表查询
    def query_by_website(self):
        self.find_element_by(*self.webiste_loc).click()
        time.sleep(1)
        self.find_element_by(*self.bibi_loc).click()
        time.sleep(1)
        self.find_element_by(*self.query_loc).click()

    # url查询
    def query_by_url(self, url):
        self.find_element_by(*self.url_loc).send_keys(url)

    # 版权名查询
    def query_by_copyright_name(self, copyrightname):
        self.find_element_by(*self.copyright_name_loc).send_keys(copyrightname)
        self.find_element_by(*self.query_loc).click()

    # 入库时间查询
    def query_by_date(self, startdate, enddate):
        self.find_element_by(*self.startdate_loc).send_keys(startdate)
        self.find_element_by(*self.enddate_loc).send_keys(enddate)
        self.find_element_by(*self.query_loc).click()

    # 审核登记
    def audit(self, uploadtime, uploaduser):
        self.find_element_by(*self.audit_loc).click()
        self.find_element_by(*self.upload_time_loc).send_keys(uploadtime)
        self.find_element_by(*self.upload_user_loc).send_keys(uploaduser)
        self.find_element_by(*self.already_tort_loc).click()
        self.find_element_by(*self.need_offline_loc).click()

        website = self.find_element_by(*self.web_loc).get_attribute('value')
        url_real = self.find_element_by(*self.url_real_loc).get_attribute('value')
        self.find_element_by(*self.confirm_loc).click()
        return website, url_real

    def query_check(self):
        self.find_element_by(*self.query_loc).click()

    def query_cnt(self):
        query_cnt = self.find_element_by(*self.query_cnt_loc).text
        return int(query_cnt.strip(query_cnt[0]+query_cnt[-1]).strip())

    def offline(self):

        self.find_element_by(*self.offline_loc).click()


# 打开侵权管理->待审核数据清单标签页
def set_window(tortaudit):
    tortaudit.open_tort_audit()
    time.sleep(2)
    return tortaudit
