from common.logger import Logging
from page_obj.base import Page



logger = Logging("lmsLoginFun").getlog()
class lmsLoginFun(Page):
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
    page_texts = [
        "https://rk98tc.e-ducation.cn/account/forget_password/",
        "Forgot password",
        "忘记密码"
    ]
    def forget_t(self):

        self.click('忘记密码')
        # print(Page_Text['lms_login'][0])
        # url = self.get_url()
        # url = url.split('/')[-2]
        # print(url)
        check = self.check_url(self.page_texts[0], self.get_url(), '忘记密码')
        self.browser_page_handle()
        return check
    def authcode_t(self):
        self.click('验证码登录')
        if self.isElementExist('验证码登录') == True:
            return True
        else:
            return False
    def translate_t(self):
        self.move('中英文切换')
        self.click('英文')
        Forgotpassword_e = self.text('忘记密码')
        self.move('中英文切换')
        self.click('中文')
        Forgotpassword_c = self.text('忘记密码')
        return Forgotpassword_e, Forgotpassword_c


