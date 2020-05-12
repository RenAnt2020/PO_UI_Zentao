from common.base_page import BasePage
from common.config import Config
from common.element_data_utils import ElementdataUtils
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    def __init__(self,driver):  #属性 ==》页面控件
        super().__init__(driver)
        # self.username_inputbox = {'element_name':'用户名输入框','locator_type':'xpath',
        #                          'locator_value':'//input[@name="account"]','timeout':15}
        # self.password_inputbox = {'element_name': '密码输入框', 'locator_type': 'xpath',
        #                          'locator_value': '//input[@name="password"]', 'timeout': 5}
        # self.login_button = {'element_name': '登录按钮', 'locator_type': 'xpath',
        #                          'locator_value': '//button[@id="submit"]', 'timeout': 5}
        elements = ElementdataUtils('login_page').get_element_info()
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']
    def input_username(self,username): #方法  ==》控件操作
        self.input(self.username_inputbox, username)
    def input_password(self,password):
        self.input(self.password_inputbox,password)
    def click_login(self):
        self.click(self.login_button)
    def clear_username(self):
        self.clear_base(self.username_inputbox)
    def get_login_fail_alert_content(self):
        return self.switch_to_alert()

if __name__ == '__main__':
    # driver = webdriver.Chrome(executable_path=Config().driver_path)  ##按driver名字启动不同的driver，并配置化
    driver = Config().driver
    login_page =  LoginPage(driver)
    login_page.open_url(Config().url)
    login_page.input_username(Config().username)
    login_page.input_password(Config().password)
    # login_page.clear_username() #调试代码
    # driver.find_element(By.XPATH, '//input[@name="account"]').clear()

    login_page.click_login()
