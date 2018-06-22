#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:liuyaqing
from selenium import webdriver
from selenium.webdriver.common.by import By
from testgroup.AutoTest.Lib.BasePage import BasePage
from testgroup.AutoTest.Projects.TXCP.all_test import *


os.environ['PATH'] += ';C:\Program Files (x86)\Tesseract-OCR'
os.environ['TESSDATA_PREFIX'] = 'C:\Program Files (x86)\Tesseract-OCR'


# 继承BasePage类
class Login(BasePage):
    # 定位器，通过元素属性定位元素对象
    username_loc = (By.XPATH, "//input[@placeholder='用户名']")
    password_loc = (By.XPATH, "//input[@placeholder='密码']")
    submit_loc = (By.XPATH, "//button[contains(.,'登录')]")
    user_loc = (By.XPATH, "//div[@class='el-dropdown']")
    sign_out_loc = (By.XPATH, "//li[contains(.,'注销')]")

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 输入用户名
    def input_username(self, username):
        # self.find_element(*self.username_loc).clear()
        self.find_element_by(*self.username_loc).send_keys(username)

    # 输入密码
    def input_password(self, password):
        # self.find_element(*self.password_loc).clear()
        self.find_element_by(*self.password_loc).send_keys(password)

    # 点击登录：调用send_keys对象，点击登录
    def click_submit(self):
        self.find_element_by(*self.submit_loc).click()

    # 定位用户登录状态
    def user_status(self):
        self.find_element_by(*self.user_loc).click()

    # 退出登录
    def sign_out(self):
        self.user_status()
        self.find_element_by(*self.sign_out_loc).click()


# 系统用户登录
def sysadmin_login():
    driver = webdriver.Chrome()
    login = Login(driver, '{web_ip}/txcp/#/login'.format(web_ip=BaseParamSet().web_address), u"通用管理平台")
    # 调用打开页面组件，输入用户名、密码
    login.open()
    login.input_username("sysadmin")
    login.input_password("Smart123")
    time.sleep(1)
    login.click_submit()  # 调用点击登录按钮组件
    time.sleep(2)
    return driver


if __name__ == '__main__':
    sysadmin_login()
