from common.base_page import BasePage
from common.login_utils import login
from element_infos.main_page import MainPage
class Testbugpape(BasePage):
    def __init__(self, driver):  # 属性 ==》页面控件
        super().__init__(driver)
        self.bug_module = {'element_name': 'BUG模块', 'locator_type': 'xpath',
                                  'locator_value': '//li[@data-id="bug"]', 'timeout': 3}
        self.createbug_button = {'element_name': '提BUG按钮', 'locator_type': 'xpath',
                                  'locator_value': '//a[contains(@href,"moduleID")]', 'timeout': 3}
        self.unclosedbug_button = {'element_name': '未关闭BUG', 'locator_type': 'xpath',
                             'locator_value': '//a[contains(@href,"unclosed.html")]', 'timeout': 3}

    def click_bug_module(self):
        self.click(self.bug_module)
    def click_createbug_button(self):
        self.click(self.createbug_button)
    def click_unclosedbug_button(self):
        self.click(self.unclosedbug_button)
if __name__=="__main__":
    login.login_success()
    main_page = MainPage(login.driver)
    main_page.goto_test()
    Testbug_pape = Testbugpape(login.driver)
    Testbug_pape.click_bug_module()
    Testbug_pape.click_unclosedbug_button()
    Testbug_pape.click_createbug_button()

