from common.base_page import BasePage
from common.login_utils import login
from element_infos.main_page import MainPage
from element_infos.testmenu_page import Testbugpape

class createbug(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.bugtitle_inputbox = {'element_name': 'BUG标题输入框', 'locator_type': 'xpath',
                           'locator_value': '//input[@id="title"]', 'timeout': 3}
        self.bugdescribe_frame= {'element_name': 'BUG描述iframe', 'locator_type': 'xpath',
                                 'locator_value': '//iframe[@class="ke-edit-iframe]', 'timeout': 3}
        self.bugdescribe_inputbox = {'element_name': 'BUG描述输入框', 'locator_type': 'xpath',
                                   'locator_value': '//body[@class="article-content"]', 'timeout': 3}
        self.submit_button = {'element_name': 'BUG提交', 'locator_type': 'xpath',
                                   'locator_value': '//button[@id="submit"]', 'timeout': 3}
    def input_bugtitle(self,bugtitle):
        self.input(self.bugtitle_inputbox,bugtitle)
    def input_bugdescribe(self,bugdescribe):
        self.frame_switch(self.bugdescribe_frame)
        self.clear(self.bugdescribe_inputbox)
        self.input(self.bugdescribe_inputbox,bugdescribe)
        self.frame_default()
    def submit_bug(self):
        self.click(self.submit_button)


if __name__=="__main__":
    login.login_success()
    main_page = MainPage(login.driver)
    main_page.goto_test()
    Testbug_pape = Testbugpape(login.driver)
    Testbug_pape.click_bug_module()
    Testbug_pape.click_unclosedbug_button()
    Testbug_pape.click_createbug_button()
    create_bug = createbug(login.driver)
    create_bug.input_bugtitle("BUG标题")
    create_bug.input_bugdescribe("这是BUG")
    create_bug.submit_bug()