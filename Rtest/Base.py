from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.log_utils import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver#启动driver
        # 元素操作封装
    def find_element(self, element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        else:
            pass
        element = WebDriverWait(self.driver, locator_timeout) \
            .until(lambda x: x.find_element(locator_type, locator_value_info))
        logger.info('[%s]元素识别成功' % element_info['element_name'])
        # element = WebDriverWait(self.driver, locator_timeout)\
        #     .until(EC.presence_of_element_located((locator_type, locator_value_info)))
        return element

    def click(self, element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('点击[%s]元素' % element_info['element_name'])

    def input(self, element_info, content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('元素[%s]输入[%s]' % (element_info['element_name'], content))
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
