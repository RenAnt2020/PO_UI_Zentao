import os
import configparser
from selenium import webdriver
from common.log_utils import logger
from selenium.webdriver.chrome.options import Options
import platform

class Config():
    def __init__(self,Env='Local'):  # 环境变量配置，取自config.ini,可配置为：Local、Test、Three
        self.Env = Env
        self.Config_path = os.path.dirname(__file__) + '/../conf/config.ini'
        self.Config = configparser.ConfigParser()
        self.Config.read(self.Config_path, encoding='utf-8')
        self.excel_path = os.path.dirname(__file__)+'/../element_infos_datas/element_infos_r.xlsx'
    @property
    def driver_path(self):
        """
        根据系统选择driver地址，注意配置地址driver文件是否存在
        """
        if platform.system() == 'Windows':
            self.Env_path = self.Config.get(self.Env, 'driver_path_win')
            self.Env_driver_path = os.path.dirname(__file__) + self.Env_path
            return self.Env_driver_path
        else:
            self.Env_path = self.Config.get(self.Env, 'driver_path_mac')
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
    @property
    def timeout(self):
        return float(self.Config.get(self.Env,"timeout"))

    """
    driver启动相关
    """
    @property
    def driver(self):
        """
        根据driver名启动对应driver，不确定Windows和Mac是不是所有driver前缀名都一样
        """
        if 'chrome' in Config().driver_path:
            return self.__get_chrome_driver()
            logger.info('使用chrome浏览器打开')
        elif 'gecko' in Config().driver_path:
            return self.__get_firefox_driver()
            logger.info('使用firefox浏览器打开')
        else:
            logger.error('webdriver启动出错。')

    def __get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension',False)  # 取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])  # 取消chrome受自动控制提示
        driver = webdriver.Chrome(options=chrome_options,executable_path=Config().driver_path)
        return driver
    def __get_firefox_driver(self):
        driver = webdriver.firefox(executable_path=Config().driver_path)
        return driver

    def __get_edge_driver(self):
        driver = webdriver.Edge(executable_path=Config().driver_path)
        return driver

    def __get_remote_driver(self):  # selenium支持分布式 grid == > 配置（你自己的代码编写、配置）
        pass

    """
    截图地址
    """
    @property
    def screenshot_path(self):
        screenshot_path_value = self.Config.get(self.Env, 'screen_shot_path')
        return screenshot_path_value

    @property
    def element_info_path(self):
        element_info_path = self.Config.get(self.Env, 'element_info_path')
        return element_info_path

    @property
    def screenshot_path(self):
        screenshot_path_value = self.Config.get(self.Env, 'screen_shot_path')
        return screenshot_path_value

    @property
    def log_path(self):
        log_path_value = self.Config.get(self.Env, 'log_path')
        return log_path_value

    @property
    def testdata_path(self):
        testdata_path_value = self.Config.get(self.Env, 'testdata_path')
        return testdata_path_value

    @property
    def case_path(self):
        case_path_value = self.Config.get(self.Env, 'case_path')
        return case_path_value

    @property
    def report_path(self):
        report_path_value = self.Config.get(self.Env, 'report_path')
        return report_path_value

    @property
    def log_level(self):
        log_level_value = int(self.Config.get('default', 'log_level'))
        return log_level_value

    @property
    def smtp_server(self):
        smtp_server_value = self.Config.get('email', 'smtp_server')
        return smtp_server_value

    @property
    def smtp_sender(self):
        smtp_sender_value = self.Config.get('email', 'smtp_sender')
        return smtp_sender_value

    @property
    def smtp_password(self):
        smtp_password_value = self.Config.get('email', 'smtp_password')
        return smtp_password_value

    @property
    def smtp_receiver(self):
        smtp_receiver_value = self.Config.get('email', 'smtp_receiver')
        return smtp_receiver_value

    @property
    def smtp_cc(self):
        smtp_cc_value = self.Config.get('email', 'smtp_cc')
        return smtp_cc_value

    @property
    def smtp_subject(self):
        smtp_subject_value = self.Config.get('email', 'smtp_subject')
        return smtp_subject_value

local_config = Config()
if __name__ == '__main__':
    print(Config().excel_path)
    print(platform.system())
    print(Config().timeout)
    print(type(Config().timeout))