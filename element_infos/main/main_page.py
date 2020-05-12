from common.base_page import BasePage
from common.login_utils import login
from common.element_data_utils import ElementdataUtils


class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements = ElementdataUtils('main').get_element_info()
        # self.companyname_showbox = {'element_name':'公司名称','locator_type':'xpath',
        #                          'locator_value':'//h1[@id="companyname"]','timeout':5}
        # self.myzone_menu = {'element_name':'我的地盘','locator_type':'xpath',
        #                          'locator_value':'//li[@data-id="my"]','timeout':5}
        # self.product_menu = {'element_name':'产品菜单','locator_type':'xpath',
        #                          'locator_value':'//li[@data-id="product"]','timeout':5}
        # self.test_menu = {'element_name':'测试菜单','locator_type':'xpath',
        #                          'locator_value':'//li[@data-id="qa"]','timeout':5}
        # self.username_showspan = {'element_name':'用户名','locator_type':'xpath',
        #                          'locator_value':'//span[@class="user-name"]','timeout':5}
        self.companyname_showbox = elements['companyname_showbox']
        self.myzone_menu = elements['myzone_menu']
        self.product_menu = elements['product_menu']
        self.test_menu = elements['test_menu']
        self.username_showspan = elements['username_showspan']
        self.myzone_link = elements['myzone_link']
        self.user_menu = elements['user_menu']
        self.quit_button = elements['quit_button']

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
    def get_username(self):
        value = self.get_text(self.user_menu)
        return value

if __name__=="__main__":
    login.login_success()
    main_page =  MainPage(login.driver)
    main_page.set_brower_max()
    main_page.goto_test()
    main_page.goto_myzone()
    main_page.set_brower_quit()
    # main_page.get_companyname() #这两句有问题还需要继续看
    # main_page.get_username()

