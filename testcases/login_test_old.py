#!/usr/bin/env python
# encoding:utf-8
# @author:Rensh
#@file:login_test.py
#@time:2020/5/12  16:51
#@desc:

import unittest
from common.base_page import BasePage
from actions.login_action import LoginAction
from common.config import Config

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.base_page = BasePage(Config().driver)
        self.base_page.set_brower_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(Config().url)

    def tearDown(self) -> None:
        self.base_page.set_brower_quit()

    # def test_login_success(self):
    #     login_action = LoginAction( self.base_page.driver )
    #     main_page = login_action.login_success('test01','newdream123')
    #     actual_result = main_page.get_username()
    #     self.assertEqual(actual_result,'测试人员1','test_login_success用例执行失败')

    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail('test01','newdream12')
        print('actual:%s'%actual_result)
        self.assertEqual(actual_result,'登录失败，请检查您的用户名或密码是否填写正确。')


if __name__ == '__main__':
    unittest.main()




