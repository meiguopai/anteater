#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : liuyaqing
import time
from testgroup.AutoTest.Lib.BasePage import BasePage
from selenium.webdriver.common.by import By


class WebSite(BasePage):
    law_loc = (By.XPATH, "//span[contains(.,'法务管理')]")
    website_loc = (By.XPATH, "//i[@class='fa fa-internet-explorer']")
    query_loc = (By.XPATH, "//button[contains(.,'查询')]")
    website_name_loc = (By.XPATH, "//input[@placeholder='网站名']")
    url_loc = (By.XPATH, "//input[@placeholder='URL']")
    source_loc = (By.XPATH, "//input[@placeholder='数据来源']")
    demand_loc = (By.XPATH, "//span[contains(.,'点播')]")
    share_loc = (By.XPATH, "//li[contains(.,'分享')]")
    search_loc = (By.XPATH, "//span[contains(.,'搜索')]")
    cloud_loc = (By.XPATH, "//span[contains(.,'云盘')]")
    thunder_loc = (By.XPATH, "//span[contains(.,'迅雷')]")
    platform_loc = (By.XPATH, "//input[@placeholder='平台']")
    pc_loc = (By.XPATH, "//li[contains(.,'PC')]")
    app_loc = (By.XPATH, "//li[contains(.,'APP')]")
    pc_app_loc = (By.XPATH, "//li[contains(.,'PC+APP')]")
    add_website_loc = (By.XPATH, "//button[contains(.,'新增')]")
    new_website_name_loc = (By.XPATH, "(//input[@type='text'])[6]")
    new_website_url_loc = (By.XPATH, "(//input[@type='text'])[7]")
    new_source_loc = (By.XPATH, "(//input[@type='text'])[8]")
    new_platforem_loc = (By.XPATH, "(//input[@type='text'])[9]")
    new_pc_loc = (By.CSS_SELECTOR, "div.el-select-dropdown:nth-child(6) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1)")
    law_contact_loc = (By.XPATH, "(//input[@type='text'])[10]")
    law_offline_explain_loc = (By.XPATH, "textarea.el-textarea__inner")
    confirm_loc = (By.XPATH, "//button[contains(.,'确 定')]")

    # 打开法务管理标签页
    def open_law(self):
        self.find_element_by(*self.law_loc).click()

    # 打卡网站管理标签页
    def open_website(self):
        self.find_element_by(*self.website_loc).click()

    # 网站名查询
    def query_by_website(self, websitename):
        self.find_element_by(*self.website_name_loc).send_keys(websitename)
        self.find_element_by(*self.query_loc).click()

    # url查询
    def query_by_url(self, url):
        self.find_element_by(*self.url_loc).send_keys(url)
        self.find_element_by(*self.query_loc).click()

    # 数据来源查询
    def query_by_source(self):
        self.find_element_by(*self.source_loc).click()
        time.sleep(1)
        self.find_element_by(*self.share_loc).click()
        time.sleep(1)
        self.find_element_by(*self.query_loc).click()

    # 平台查询
    def query_by_platform(self):
        self.find_element_by(*self.platform_loc).click()
        time.sleep(1)
        self.find_element_by(*self.pc_loc).click()
        time.sleep(1)
        self.find_element_by(*self.query_loc).click()

    # 新增站点
    def add_website(self, website, source):
        self.find_element_by(*self.add_website_loc).click()
        time.sleep(1)
        self.find_element_by(*self.new_website_name_loc).send_keys(website)
        # self.find_element_by(*self.new_website_url_loc).send_keys(url)
        time.sleep(1)
        self.find_element_by(*self.new_source_loc).send_keys(source)
        time.sleep(1)
        self.find_element_by(*self.new_platforem_loc).click()
        time.sleep(1)
        self.find_element_by(*self.new_pc_loc).click()
        time.sleep(1)
        self.find_element_by(*self.confirm_loc).click()

    def result_value(self):
        return self.find_element_by(*(By.XPATH, "//tr[@class='el-table__row']")).text

    def page_value(self):
        return self.find_element_by(*(By.XPATH, "//span[@class='el-pagination__total']")).text


# 打开法务管理->网站管理标签页
def set_window(website):
    website.open_law()
    time.sleep(1)
    website.open_website()
    time.sleep(1)
    return website
