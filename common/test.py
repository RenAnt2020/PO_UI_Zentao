#!/usr/bin/env python
# encoding:utf-8
# @author:Rensh
#@file:test.py
#@time:2020/5/12  10:11
#@desc:
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.base_page import BasePage
from common.config import Config

driver = Config().driver
test = BasePage(driver)
test.open_url('C:/Users/AntMi/Desktop/python%E5%AD%A6%E4%B9%A0/Selenium/element_samples.html')
alterbutton = {'element_name':'alterbutton','locator_type':'xpath',
                                 'locator_value':'//input[@name="alterbutton"]','timeout':5}
promptbutton = {'element_name':'promptbutton','locator_type':'xpath',
                                 'locator_value':'//input[@name="promptbutton"]','timeout':5}
# test.click(alterbutton)
# test.switch_to_alert()
test.click(promptbutton)
test.input_alert('test')
# test.switch_to_alert('dismiss')
# test.open_url("http://www.baidu.com")
# if EC.title_contains('baidu'):
#     news = {'element_name':'news','locator_type':'xpath',
#                                      'locator_value':'//a[@href="http://news.baidu.com"]','timeout':5}
#     handle = test.get_window_handle()
#     test.click(news)
#     test.switch_to_window_by_handle(handle)
#     test.switch_to_window_by_title('e')
    # test.switch_to_window_by_url('http://news.baidu.com/')
    # window_handles = driver.window_handles  # 获取当前窗口属句柄集合（列表类型）
    # print(window_handles)
    # print(EC.title_contains('news.baidu.com'))
    # for window_handle in window_handles:  # window_handle需要传进来吧，只是用来做循环，其实问题不大
    #     if WebDriverWait(driver, Config().timeout).until(EC.title_contains('news.baidu.com')):
    #         test.switch_to.window(window_handle)