import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.log_utils import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver#启动driver
    #浏览器操作封装
    def open_url(self,url):
        logger.info("打开网址：[%s]"%url)
        self.driver.get(url)
    def set_brower_max(self):
        logger.info("浏览器最大化")
        self.driver.maximize_window()
    def set_brower_min(self):
        logger.info("浏览器最小化")
        self.driver.minimize_window()
    def refresh(self):
        logger.info("浏览器刷新")
        self.driver.refresh()
    def get_title(self):
        title = self.driver.title
        logger.info("浏览器title：[%s]" %title)
        return title
    def get_text(self):
        text = self.driver.text
        logger.info("浏览器title：[%s]" %text)
        return text
    def set_brower_quit(self):
        self.driver.quit()
        logger.info('浏览器退出')
    #元素操作封装
    def find_element(self,element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        else:pass
        element = WebDriverWait(self.driver, locator_timeout) \
            .until(lambda x: x.find_element(locator_type, locator_value_info))
        logger.info('[%s]元素识别成功' % element_info['element_name'])
        # element = WebDriverWait(self.driver, locator_timeout)\
        #     .until(EC.presence_of_element_located((locator_type, locator_value_info)))
        return element

    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('点击[%s]元素'%element_info['element_name'])

    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('元素[%s]输入[%s]' % (element_info['element_name'],content))
    def frame_switch(self,element_info):
        content_frame = self.find_element(element_info)
        self.driver.switch_to.frame(content_frame)
        logger.info('切换Frame到[%s]' % element_info['element_name'])
    def frame_default(self):
        self.driver.switch_to.default_content()
        logger.info('回到默认主Frame')
    def clear_base(self,element_info):
        element = self.find_element(element_info)
        element.clear()
        logger.info('[%s]输入框清楚'% element_info['element_name'])
    #鼠标操作
    #按传入的JS代码操作
    def execute_script(self,js_str,element_info=None):
        if element_info:
            element = self.find_element(element_info)
            self.driver.execute_script(js_str,element)
        else:
            self.driver.execute_script(js_str,None)
    #滚动条拖动到页面元素位置
    def scrollIntoView_script(self,element_info):
        element = self.find_element(element_info)
        self.driver.execute_script("return arguments[0].scrollIntoView();",element)





if __name__ == '__main__':
    pass


