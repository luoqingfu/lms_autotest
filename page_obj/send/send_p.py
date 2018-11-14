import random

from common.function import Random
from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig

logger = Logging('studyCourse').getlog()
config = ReadConfig()
class test_s(Page, Random):
    def __init__(self,driver):
        Page.__init__(self,driver)
        self.config_element = {
            '账号输入':['css', '#app > div.container > div:nth-child(1) > div.up-layer > div:nth-child(2) > input'],
            '密码输入':['css', '#app > div.container > div:nth-child(1) > div.up-layer > div:nth-child(3) > input'],
            '确认':['css', '#app > div.container > div:nth-child(1) > div.up-layer > div:nth-child(4) > button'],
            '输入':['css', '#mywords'],
            'send':['id', 'jssend'],
        }

    def login(self):
        # 登录方法
        self.send_keys('账号输入', '13226349780')
        self.send_keys("密码输入", '000001')
        self.click("确认")
        self.wait_time(2)


    def send_msg(self):
        self.send_keys('输入','1111111111')
        self.click('send')












