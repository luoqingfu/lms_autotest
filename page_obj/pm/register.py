from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig

config = ReadConfig()
logger = Logging('perpmRegister').getlog()
class perpmRegister(Page):
    def __init__(self,driver):
        Page.__init__(self,driver)
        self.config_element = {
            "账号输入框": ["id", "reg_user_email"],
            "密码输入框": ['id', "login_password"],
            "登录按钮": ['xpath', "/html/body/div[1]/div[2]/div/div[1]/div/form/div[1]/button"],
            "登录错误提示": ['id', 'reg_msg'],
            "忘记密码": ['id', 'forget_password'],
            "验证码登录": ['css', 'body > div.company-login.login01 > div > div.login-panel-body > form > div.tips > div > a.pull-right.code-btn'],
            "账号密码登录": ['id', 'accout-login'],
            "中英文切换": ['css', 'body > div.language > ul > li.language-active > a'],
            "英文": ['linktext', 'English'],
            "中文": ['linktext', '中文'],
            "登录按钮_1": ['xpath', '/html/body/nav/div/div[2]/ul[3]/li[2]/button']

        }
    page_texts = [
            '13070092361', '14570092361','14670092361','14770092361','14870092361','14970092361',
            '15070092361',
            '15170092361',
            '15270092361',
            '15370092361',
            '15470092361',
            '15570092361',
            '15670092361',
            '15770092361',
            '15870092361',
            '15970092361',
            '16570092361',
            '16670092361',
            '17070092361',
            '17170092361',
            '17270092361',
            '17370092361',
            '17470092361',
            '17570092361',
            '17670092361',
            '17770092361',
            '17870092361',
            '17970092361',
            '18070092361',
            '18170092361',
            '18270092361',
            '18370092361',
            '18470092361',
            '18570092361',
            '18670092361',
            '18770092361',
            '19870009236',
            '19970009236',
            '18870092361',
            '18970092361',
            '13170092361',
            '13270092361',
            '13370092361',
            '13470092361',
            '13570092361',
            '13670092361',
            '13770092361',
            '13870092361',
            '13970092361',
            'zz.liu49@eliteu.com.cn'

        ]
    def cli(self):
        self.click('登录按钮_1')

    def per_login_test(self,n):

        username = self.page_texts[n]
        self.cli()
        self.send_keys('账号输入框', username)

        self.click("登录按钮")
        show_error = ''
        if self.isElementExist('登录错误提示') == True:
            show_error = self.text('登录错误提示')
            logger.error('登录错误')
        self.browser_page_handle('0')

        return show_error
