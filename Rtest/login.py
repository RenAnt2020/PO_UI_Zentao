from Rtest.Base import BasePage
class LoginPage(BasePage):
    def __init__(self,driver):  #属性 ==》页面控件
        super().__init__(driver) #父类的driver
        self.username_inputbox = {'element_name':'用户名输入框','locator_type':'xpath',
                                 'locator_value':'//input[@name="account"]','timeout':15}
        self.password_inputbox = {'element_name': '密码输入框', 'locator_type': 'xpath',
                                 'locator_value': '//input[@name="password"]', 'timeout': 5}
        self.login_button = {'element_name': '登录按钮', 'locator_type': 'xpath',
                                 'locator_value': '//button[@id="submit"]', 'timeout': 5}
    def input_username(self,username):#方法  ==》控件操作
        self.input(self.username_inputbox, username)
    def input_password(self,password):
        self.input(self.password_inputbox,password)
    def click_login(self):
        self.click(self.login_button)


