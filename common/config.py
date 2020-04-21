import os
import configparser
from selenium import webdriver
from common.log_utils import logger

class Config():
    def __init__(self,Env='Local'):
        self.Env = Env
        self.Config_path = os.path.dirname(__file__) + '/../conf/config.ini'
        self.Config = configparser.ConfigParser()
        self.Config.read(self.Config_path, encoding='utf-8')
    @property
    def driver_path(self):
        self.Env_path = self.Config.get(self.Env, 'driver_path')
        self.Env_driver_path = os.path.dirname(__file__) + self.Env_path
        return self.Env_driver_path
    @property
    def url(self):
        return self.Config.get(self.Env,'url')
    @property
    def username(self):
        return self.Config.get(self.Env,'username')
    @property
    def password(self):
        return self.Config.get(self.Env,"password")

    def driver(self):
        if  'chrome' in Config().driver_path:
            self.driver = webdriver.Chrome(executable_path=Config().driver_path)  ##按driver名字启动不同的driver，并配置化
            logger.info('使用chrome浏览器打开')
        elif 'gecko' in Config().driver_path:
            self.driver = webdriver.firefox(executable_path=Config().driver_path)
            logger.info('使用firefox浏览器打开')
        else:
            logger.error('webdriver启动出错。')
        return self.driver


if __name__ == '__main__':
    print(Config().driver())