#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:liuyaqing
import time
from pykeyboard import PyKeyboard
from selenium.webdriver.common.by import By
from testgroup.AutoTest.Lib.BasePage import BasePage


class GroupManagement(BasePage):
    system_loc = (By.XPATH, "//span[contains(.,'系统管理')]")
    group_loc = (By.XPATH, "//i[@class='fa fa-group']")
    # 新增分组
    add_group_loc = (By.XPATH, "//button[contains(.,'新增分组')]")
    group_name_loc = (By.CSS_SELECTOR, "input.el-input__inner")
    group_describe_loc = (By.XPATH, "(//input[@type='text'])[2]")
    confirm_loc = (By.XPATH, "//button[contains(.,'确 定')]")
    # 修改分组
    modify_group_loc = (By.XPATH, "(//button[@type='button'])[13]")
    # 配置菜单
    authority_loc = (By.XPATH, "(//button[@type='button'])[14]")
    # tort_box_loc = (By.XPATH, "//span[contains(.,'系统管理')]")
    tort_box_loc = (By.CSS_SELECTOR, "span.el-checkbox__inner")
    ok_loc = (By.XPATH, "(//button[@type='button'])[21]")
    # 删除分组
    del_group_loc = (By.XPATH, "(//button[@type='button'])[15]")

    # 打开系统管理菜单
    def open_system(self):
        self.find_element_by(*self.system_loc).click()

    # 打开分组管理菜单
    def open_group(self):
        self.find_element_by(*self.group_loc).click()

    # 新增分组
    def add_group(self, groupname, groupdescribe):
        self.find_element_by(*self.add_group_loc).click()
        self.find_element_by(*self.group_name_loc).send_keys(groupname)
        self.find_element_by(*self.group_describe_loc).send_keys(groupdescribe)
        self.find_element_by(*self.confirm_loc).click()

    # 修改分组信息
    def modify_group(self, groupname, groupdescribe):
        self.find_element_by(*self.modify_group_loc).click()
        time.sleep(1)
        name = self.find_element_by(*self.group_name_loc)
        name.clear()
        name.send_keys(groupname)
        time.sleep(1)
        describe = self.find_element_by(*self.group_describe_loc)
        time.sleep(1)
        describe.clear()
        describe.send_keys(groupdescribe)
        time.sleep(1)
        self.find_element_by(*self.confirm_loc).click()

    # 配置菜单
    def configure_authority(self):
        self.find_element_by(*self.authority_loc).click()
        time.sleep(2)
        self.find_element_by(*self.tort_box_loc).click()
        time.sleep(1)
        self.find_element_by(*self.ok_loc).click()
        time.sleep(2)
        k = PyKeyboard()
        k.tap_key(k.enter_key)

    # 判断是否被选择
    def if_selected(self):
        self.find_element_by(*self.authority_loc).click()
        time.sleep(2)
        re = self.find_element_by(*self.tort_box_loc).is_selected()
        return re

    # 删除分组
    def del_group(self):
        time.sleep(1)
        self.find_element_by(*self.del_group_loc).click()
        time.sleep(2)
        k = PyKeyboard()
        k.tap_key(k.enter_key)


# 打开系统管理->分组管理标签页
def set_window(group):
    group.open_system()
    time.sleep(1)
    group.open_group()
    time.sleep(2)
    return group
