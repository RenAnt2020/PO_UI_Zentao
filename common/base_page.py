import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import HTMLTestReportCN
from common.log_utils import logger
from common.config import Config

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver  # 启动driver
    """
    浏览器操作封装
    """
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
    def close_tab(self):
        self.driver.close()
        logger.info('关闭当前的tab页签')

    """
    根据提供的元素信息，进行元素查找与操作
    """
    def find_element(self,element_info):
        """
        :param element_info: 元素信息，字典类型{...}
        :return:element 可以查找的对象
        """
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
    """
    页面元素操作封装
    """
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

    """
    按JS代码进行操作
    """
    def execute_script(self,js_str,element_info=None):
        """
        :param js_str: JS操作代码，如："return arguments[0].scrollIntoView();"
        :param element_info: 元素信息，字典类型{...}
        """
        if element_info:
            element = self.find_element(element_info)
            self.driver.execute_script(js_str,element)
        else:
            self.driver.execute_script(js_str,None)

    def scrollIntoView_script(self,element_info):
        """
        将滚动条移动到指定位置
        :param element_info: 元素信息，字典类型{...}
        :return:
        """
        element = self.find_element(element_info)
        self.driver.execute_script("return arguments[0].scrollIntoView();",element)



    """
    alert处理
    """
    def switch_to_alert(self,action='accept',time_out=Config().timeout):
        WebDriverWait(self.driver,time_out).until(EC.alert_is_present())
        alter = self.driver.switch_to.alert
        alter_text = alter.text
        if action == 'accept':
            alter.accept()
            logger.info('点击弹框的确认按钮')
        elif action == 'dismiss':
            alter.dismiss()
            logger.info('点击弹框的取消按钮')
        return alter_text
    """
    prompt对话框内容输入
    """
    def input_prompt(self,content):
        self.driver.send_keys(content)


    """
       windows句柄操作
    """
    def get_window_handle(self):
        handle = self.driver.current_window_handle  # current_window_handle获取当前页面句柄
        logger.info('获取句柄:%s'%handle)
        return handle

    def switch_to_window_by_handle(self,window_handle):
        self.driver.switch_to.window(window_handle)  # driver.switch_to.window(handles[num]) # 跳转到第num个窗口，从0开始
        logger.info("跳转到句柄:%s"%window_handle)

    # 调试未通过
    def switch_to_window_by_title(self,title):
        window_handles = self.driver.window_handles  # 获取当前窗口属句柄集合（列表类型）
        for window_handle in window_handles:  # window_handle需要传进来吧，只是用来做循环，其实问题不大
            # self.driver.switch_to.window(window_handle)
            if WebDriverWait(self.driver,Config().timeout).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                logger.info("跳转到title:%s的窗口"%title)
                break
    def switch_to_window_by_url(self,url):
        window_handles = self.driver.window_handles  # 获取当前窗口属句柄集合（列表类型）
        for window_handle in window_handles:  # window_handle是用来做循环
            if WebDriverWait(self.driver,Config().timeout).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                logger.info("跳转到url:%s的窗口" %url)
                break

    """
    键盘、鼠标常用操作
    """
    def move_to_element_by_mouse(self,element_info):
        element = self.find_element(element_info)
        self.chains.move_to_element(element).perform()

    def long_press_element(self,element_info,senconds):
        element = self.find_element(element_info)
        self.chains.click_and_hold(element).pause(senconds).release(element)
    """
    截图、等待
    """
    def screenshot_as_file(self):
        report_path = os.path.join( os.path.abspath(os.path.dirname(__file__)) , '..', local_config.report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot( self.driver )

    def screenshot_as_file_old(self, *screenshot_path):
        current_dir = os.path.dirname(__file__)
        if len(screenshot_path) == 0:
            screenshot_filepath = Config().screenshot_path
        else:
            screenshot_filepath = screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        screenshot_filepath = os.path.join(current_dir, '..' ,screenshot_filepath, 'UITest_%s.png' % now)
        self.driver.get_screenshot_as_file(screenshot_filepath)

    def wait(self,seconds=Config().timeout):
        time.sleep(seconds)

    def implicitly_wait(self, seconds=Config().timeout):
        self.driver.implicitly_wait(seconds)
if __name__ == '__main__':
    test = BasePage(Config().driver)
    test.open_url('C:/Users/AntMi/Desktop/python%E5%AD%A6%E4%B9%A0/Selenium/element_samples.html')


