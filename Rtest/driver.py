import os
from selenium import webdriver
from Rtest.login import LoginPage

Firefox_path = os.path.dirname(__file__) + '/../webdriver/' + "geckodriver.exe"
driver = webdriver.Firefox(executable_path=Firefox_path)
driver.implicitly_wait(15)
LoginPage(driver).open_url('http://127.0.0.1/zentao/user-login.html')
LoginPage(driver).input_username("admin")
LoginPage(driver).input_password("A12345678")
LoginPage(driver).click_login()



