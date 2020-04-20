import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.config import Config
from common.base_page import BasePage
from common.login_utils import login
from element_infos.login_page import LoginPage

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.companyname_showbox = {'element_name':'用户名输入框','locator_type':'xpath',
                                 'locator_value':'//h1[@id="companyname"]','timeout':5}
        self.myzone_menu = {'element_name':'用户名输入框','locator_type':'xpath',
                                 'locator_value':'//li[@data-id="my"]','timeout':5}
        self.product_menu = {'element_name':'用户名输入框','locator_type':'xpath',
                                 'locator_value':'//li[@data-id="product"]','timeout':5}
        self.test_menu = {'element_name':'测试菜单','locator_type':'xpath',
                                 'locator_value':'//li[@data-id="qa"]','timeout':5}
        self.username_showspan = {'element_name':'用户名输入框','locator_type':'xpath',
                                 'locator_value':'//span[@class="user-name"]','timeout':5}
    # def get_companyname(self):  # 获取公司名称
    #     value = self.get_title(self.companyname_showbox)
    #     return value

    def goto_myzone(self):  # 进入我的地盘菜单
        self.click(self.myzone_menu)

    def goto_test(self):  # 进入测试菜单
        self.click(self.test_menu)

    def goto_product(self):  # 进入产品菜单
        self.click(self.product_menu)

    # def get_username(self):
    #     value = self.get_text(self.username_showspan)
    #     logger.info('获取用户名成功，用户名是：' + str(value) )
    #     return value

if __name__=="__main__":
    # driver = webdriver.Chrome(executable_path=Config().driver_path)  ##按driver名字启动不同的driver，并配置化
    # login_page =  LoginPage(driver)
    # login_page.open_url(Config().url)
    # login_page.input_username(Config().username)
    # login_page.input_password(Config().password)
    # login_page.click_login()
    login().login_success()
    main_page =  MainPage(login().driver)
    main_page.goto_test()
    main_page.goto_myzone()
    # main_page.get_companyname() #这两句有问题还需要继续看
    # main_page.get_username()
