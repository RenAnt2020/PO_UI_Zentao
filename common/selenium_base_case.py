#!/usr/bin/env python
# encoding:utf-8
# @author:Rensh
#@file:selenium_base_case.py
#@time:2020/5/12  16:43
#@desc:
import unittest
from common.base_page import BasePage
from common.config import Config
from common.log_utils import logger

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info('')
        logger.info('==============测试类开始执行=============')
        cls.url = Config().url

    def setUp(self) -> None:
        logger.info('---------测试方法开始执行-----------')
        self.base_page = BasePage(Config().driver)
        self.base_page.set_brower_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(Config().url)

    def tearDown(self) -> None:
        # 测试用例失败截图
        # if len(self._outcome.errors)>=1:
        #     self.base_page.screenshot_as_file()
        errors = self._outcome.errors
        for test,exc_info in errors:
            if exc_info:
                self.base_page.wait()
                self.base_page.screenshot_as_file()
        self.base_page.close_tab()
        logger.info('---------测试方法执行完毕-----------')

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('==============测试类执行完毕=============')
