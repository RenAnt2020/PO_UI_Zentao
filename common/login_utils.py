from element_infos.login.login_page import LoginPage
from common.config import Config


class login(object):
    def __init__(self):
        self.driver = Config().driver
    def login_success(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.open_url(Config().url)
        self.login_page.input_username(Config().username)
        self.login_page.input_password(Config().password)
        self.login_page.click_login()
# login = login()

if __name__ == '__main__':
    login.login_success()