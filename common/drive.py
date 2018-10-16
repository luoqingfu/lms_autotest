import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import readConfig
from common.logger import Logging
logger = Logging("Driver").getlog()
dir = readConfig.ProjectPath        #获取配置文件所在的文件路径
class Driver():
    """选择加载浏览器的驱动"""
    #firefox_driver_path = dir+ '/driver/geckodriver.exe'
    #chrome_driver_path = dir + '/driver/chromedriver.exe'
    #ie_driver_path = dir + '/driver/IEDriverServer.exe'
    """修改为mac os驱动路经"""
    firefox_driver_path = dir + '/driver/geckodriver'
    chrome_driver_path = dir + '/driver/chromedriver'
    def __init__(self, driver, time = 15):
        self.driver = driver
        self.time = time
    def open_browser(self):
        """打开浏览器"""
        if self.driver == "Firefox" or self.driver == "firefox":
            self.browser = webdriver.Firefox(self.firefox_driver_path)
            logger.info("打开火狐浏览器")
        if self.driver == "Chrome":
            self.browser = webdriver.Chrome(self.chrome_driver_path)
            logger.info("打开谷歌浏览器")
        #if self.driver == "IE":
           # self.browser = webdriver.Ie(self.ie_driver_path)
           # logger.info("打开IE浏览器")
        if self.driver == "JS":
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.implicitly_wait(self.time)
        logger.info("隐式等待元素时间为：{}".format(self.time))
        return  self.browser

if __name__ == '__main__':
    dir = os.path.dirname(os.path.abspath(''))  # 注意相对路径获取方法
    print(dir, "dir")