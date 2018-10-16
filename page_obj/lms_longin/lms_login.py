from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig

config = ReadConfig()
logger = Logging('LmsLogin').getlog()
class LmsLogin(Page):
    def __init__(self,driver):
        Page.__init__(self,driver)
        self.config_element = {
            "账号输入框": ["id", "login_user_email"],
            "密码输入框": ['id', "login_password"],
            "登录按钮": ['css', "body > div.company-login.login01 > div > div.login-panel-body > form > div.form-group.no-margin-bot > div > button"],
            "登录错误提示": ['id', 'show_error'],
            "忘记密码": ['id', 'forget_password'],
            "验证码登录": ['css', 'body > div.company-login.login01 > div > div.login-panel-body > form > div.tips > div > a.pull-right.code-btn'],
            "账号密码登录": ['id', 'accout-login'],
            "中英文切换": ['css', 'body > div.language > ul > li.language-active > a'],
            "英文": ['linktext', 'English'],
            "中文": ['linktext', '中文'],

        }
    def lms_login_test(self):
        username = config.getConfig('username')
        password = config.getConfig('password')
        self.send_keys('账号输入框', username)
        self.send_keys("密码输入框", password)
        self.click("登录按钮")
        show_error = ''
        if self.isElementExist('登录错误提示') == True:
            show_error = self.text('登录错误提示')
            logger.error('登录错误')


        return show_error
