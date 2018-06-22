#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:liuyaqing
import time
from pykeyboard import PyKeyboard
from selenium.webdriver.common.by import By
from testgroup.AutoTest.Lib.BasePage import BasePage


class UserManagement(BasePage):
    system_loc = (By.XPATH, "//span[contains(.,'系统管理')]")
    user_loc = (By.XPATH, "//i[@class='fa fa-user']")
    # 新增用户
    add_user_loc = (By.XPATH, "//button[contains(.,'新增用户')]")
    username_loc = (By.CSS_SELECTOR, "div.el-form-item__content > div.el-input.el-input--mini > input.el-input__inner")
    name_loc = (By.XPATH, "(//input[@type='text'])[3]")
    password_loc = (By.XPATH, "(//input[@type='text'])[4]")
    group_loc = (By.XPATH, "(//input[@type='text'])[5]")
    admin_loc = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]')
    confirm_loc = (By.XPATH, "//button[contains(.,'确 定')]")
    # 修改用户
    modify_user_loc = (By.XPATH, "//button[contains(.,'修改')]")
    # 删除用户
    del_user_loc = (By.XPATH, "//button[contains(.,'删除')]")

    # 打开系统管理标签页
    def open_system(self):
        self.find_element_by(*self.system_loc).click()

    # 打开用户管理标签页
    def open_user(self):
        self.find_element_by(*self.user_loc).click()

    # 新增用户
    def add_user(self, username, name, password):
        self.find_element_by(*self.add_user_loc).click()
        time.sleep(2)
        self.find_element_by(*self.username_loc).send_keys(username)
        self.find_element_by(*self.name_loc).send_keys(name)
        pwd = self.find_element_by(*self.password_loc)
        pwd.clear()
        pwd.send_keys(password)
        self.find_element_by(*self.group_loc).click()
        self.find_element_by(*self.admin_loc).click()
        self.find_element_by(*self.confirm_loc).click()

    # 修改用户
    def modify_user(self, nname):
        self.find_element_by(*self.modify_user_loc).click()
        time.sleep(2)
        name = self.find_element_by(*self.name_loc)
        name.clear()
        name.send_keys(nname)
        self.find_element_by(*self.confirm_loc).click()

    # 删除用户
    def del_user(self, driver):
        self.find_element_by(*self.del_user_loc).click()
        time.sleep(2)
        k = PyKeyboard()
        k.tap_key(k.enter_key)


# 打开系统管理->用户管理标签页
def set_window(user):
    user.open_system()
    time.sleep(1)
    user.open_user()
    time.sleep(2)
    return user
