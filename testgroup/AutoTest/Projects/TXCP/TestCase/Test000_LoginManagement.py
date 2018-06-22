#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:liuyaqing
from selenium import webdriver
from testgroup.AutoTest.Projects.TXCP.Pages import LoginPage
from testgroup.AutoTest.Projects.TXCP.all_test import *


class Login(unittest.TestCase):
    """ 登录管理模块测试 """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.web_ip = BaseParamSet().web_address
        cls.login = LoginPage.Login(cls.driver, '{web_ip}/txcp/#/login'.format(web_ip=cls.web_ip), u"通用管理平台")
        cls.username = 'sysadmin'
        cls.password = 'Smart123'

    def test_01_login_sucess(self):
        """ 用户登陆 """
        # 调用打开页面组件，输入用户名、密码
        self.login.open()
        self.login.input_username(self.username)
        self.login.input_password(self.password)
        time.sleep(1)
        self.login.click_submit()  # 调用点击登录按钮组件
        time.sleep(1)
        self.assertEqual(self.driver.current_url, '{web_ip}/txcp/#/'.format(web_ip=self.web_ip))

    def test_02_sign_out(self):
        """ 退出登录 """
        self.login.sign_out()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, '{web_ip}/txcp/#/login'.format(web_ip=self.web_ip))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
