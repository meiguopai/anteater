#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:liuyaqing
from testgroup.AutoTest.Projects.TXCP.all_test import *
from testgroup.AutoTest.Projects.TXCP.Pages import LoginPage
from testgroup.AutoTest.Projects.TXCP.Pages import UserManagementPage
from testgroup.AutoTest.Projects.TXCP.DB import OperateDB


class UserManagement(unittest.TestCase):
    """ 用户管理模块测试 """
    @classmethod
    def setUpClass(cls):
        cls.driver = LoginPage.sysadmin_login()
        cls.user = UserManagementPage.set_window(
            UserManagementPage.UserManagement(cls.driver, '{web_ip}/txcp/#/login'.format(web_ip=BaseParamSet().web_address), u"通用管理平台"))
        cls.test_username = 'lyq01'
        cls.test_name = 'liuyaqing01'
        cls.test_password = 'sa'
        cls.test_modify_name = 'liuyaqing001'

    def test_01_add_user(self):
        """ 新增用户 """
        self.user.add_user(self.test_username, self.test_name, self.test_password)
        time.sleep(1)
        results = OperateDB.mysql_execute("SELECT user_name FROM t_sys_user")
        self.assertTrue(results.__contains__((self.test_username,)))

    def test_02_modify_user(self):
        """ 修改用户 """
        self.user.modify_user(nname=self.test_modify_name)
        time.sleep(1)
        results = OperateDB.mysql_execute("SELECT real_name FROM t_sys_user WHERE user_name='%s';" % self.test_username)
        self.assertTrue(results.__contains__((self.test_modify_name,)))

    def test_03_del_user(self):
        """ 删除用户 """
        self.user.del_user(self.driver)
        time.sleep(1)
        results = OperateDB.mysql_execute("SELECT user_name FROM t_sys_user;")
        self.assertFalse(results.__contains__((self.test_username,)))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
