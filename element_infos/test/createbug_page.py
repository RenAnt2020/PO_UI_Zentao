from common.base_page import BasePage
from common.login_utils import login
from element_infos.main.main_page import MainPage
from element_infos.test.testmenu_page import Testbugpape
from common.element_date_utils import ElementdataUtils

class createbug(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.bugtitle_inputbox = {'element_name': 'BUG标题输入框', 'locator_type': 'xpath',
        #                    'locator_value': '//input[@id="title"]', 'timeout': 3}
        # self.bugdescribe_frame= {'element_name': 'BUG描述iframe', 'locator_type': 'xpath',
        #                          'locator_value': '//iframe[@class="ke-edit-iframe"]', 'timeout': 3}
        # self.bugdescribe_inputbox = {'element_name': 'BUG描述输入框', 'locator_type': 'xpath',
        #                            'locator_value': '//body[@class="article-content"]', 'timeout': 3}
        # self.submit_button = {'element_name': 'BUG提交', 'locator_type': 'xpath',
        #                            'locator_value': '//button[@id="submit"]', 'timeout': 3}
        # self.version_chosen = {'element_name': '影响版本选择', 'locator_type': 'xpath',
        #                            'locator_value': '//div[@id="openedBuild_chosen"]', 'timeout': 3}
        # self.version = {'element_name': '影响版本', 'locator_type': 'xpath',
        #                        'locator_value': '//li[@title="主干"]', 'timeout': 3}
        elements = ElementdataUtils('createbug_page').get_element_info()
        self.bugtitle_inputbox = elements['bugtitle_inputbox']
        self.bugdescribe_frame = elements['bugdescribe_frame']
        self.submit_button = elements['submit_button']
        self.bugdescribe_inputbox = elements['bugdescribe_inputbox']
        self.version_chosen = elements['version_chosen']
        self.version = elements['version']

    def input_bugtitle(self,bugtitle):
        self.input(self.bugtitle_inputbox,bugtitle)
    def frame_switch_creat(self):
        self.frame_switch(self.bugdescribe_frame)
    def clear_creat(self):
        self.clear_base(self.bugdescribe_inputbox)
    def input_bugdescribe(self,bugdescribe):
        self.frame_switch(self.bugdescribe_frame)
        self.clear_base(self.bugdescribe_inputbox)
        self.input(self.bugdescribe_inputbox,bugdescribe)
        self.frame_default()
    def submit_bug(self):
        self.click(self.submit_button)
    def version_ch(self):
        self.click(self.version_chosen)
        self.click(self.version)


if __name__=="__main__":
    login.login_success()
    main_page = MainPage(login.driver)
    main_page.goto_test()
    Testbug_pape = Testbugpape(login.driver)
    Testbug_pape.click_bug_module()
    Testbug_pape.click_unclosedbug_button()
    Testbug_pape.click_createbug_button()
    create_bug = createbug(login.driver)
    create_bug.version_ch()
    create_bug.input_bugtitle("BUG标题")
    # create_bug.frame_switch_creat()
    # create_bug.clear_creat()
    create_bug.input_bugdescribe("这是BUG")#缺少form转换
    # create_bug.execute_script("return arguments[0].scrollIntoView();",create_bug.submit_button)
    create_bug.scrollIntoView_script(create_bug.submit_button)
    create_bug.submit_bug()
