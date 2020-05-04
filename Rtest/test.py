from Rtest.login import LoginPage
from Rtest.driver import set_driver
from selenium.webdriver.common.by import By

driver = set_driver()
LoginPage(driver).username_inputbox('admin')

# def login(driver,username,password):
#     driver.find_element(By.XPATH, '//input[@type="text"]').send_keys(username)
#     driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
#     driver.find_element(By.XPATH, '//button[@type="button"]').click()

