import random

from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig


logger = Logging('change_pwd').getlog()
config = ReadConfig()
class change_pwd(Page):
    def __init__(self, driver):
        Page.__init__(self,driver)
        self.config_element = {
            "账号输入框": ["id", "login_user_email"],
            "密码输入框": ['id', "login_password"],
            "登录按钮": ['css',
                     "body > div.company-login.login01 > div > div.login-panel-body > form > div.form-group.no-margin-bot > div > button"],
            "登录错误提示": ['id', 'show_error'],
            "忘记密码": ['id', 'forget_password'],
            "验证码登录": ['css',
                      'body > div.company-login.login01 > div > div.login-panel-body > form > div.tips > div > a.pull-right.code-btn'],
            "账号密码登录": ['id', 'accout-login'],
            "中英文切换": ['css', 'body > div.language > ul > li.language-active > a'],
            "英文": ['linktext', 'English'],
            "中文": ['linktext', '中文'],
            "地址管理": ['css', '#myTabs > li:nth-child(3) > a'],
            "个人资料入口": ['css', '#hover-drop > a > img'],
            "个人资料": ['css', '#hover-drop > ul > li:nth-child(2) > a'],
            "添加新地址": ['css', '#tab3 > div > div > div > button'],

            "选择图片": ['id', 'chooseuserpic'],
            "昵称": ['id', 'nickname'],
            "最高学历": ['css', '#profile_form > div:nth-child(4) > div > div > span'],
            "博士学位": ['css', 'span.selecter-item'],
            "保存": ['id', 'save_user_info'],
            "账号安全": ['css', '#myTabs > li.active'],
            "绑定邮箱": ['id', 'click_change_email'],
            "邮件_密码输入框": ['id', 'email_oldpassword'],
            "修改邮箱": ['id', 'new_email'],
            "发送邮件": ['id', 'send_email'],
            "邮箱_取消": ['css', '#cancel_email_send > div > input'],
            "邮箱密码_错误提示": ['id', 'email_oldpassword-error'],
            "邮箱_错误": ['id', 'new_email-error'],
            "修改手机": ['id', 'click_change_mobile'],
            "修改手机_old": ['id', 'phone_oldpassword'],
            "修改手机_手机号码": ['id', 'mobile'],
            "修改手机_弹窗": ['css', '#layui-layer10 > div.layui-layer-btn > a'],
            "手机_获取验证码": ['id', 'get_verification_code'],
            "修改手机提交": ['id', 'submit_change_mobile'],
            "手机_取消": ['css', '#now_change_phone > div:nth-child(4) > div > input.btn.btn-primary.cancel-change'],
            "重置密码": ['id', 'click_change_password'],
            "原密码输入框": ['id', 'psw-old'],
            "原密码错误提示": ['id', 'psw-old-error'],
            "新密码": ['id', 'change_psw1'],
            "新密码错误提示": ['id', 'change_psw1-error'],
            "确认密码输入框": ['id', 'change_psw2'],
            "确认密码错误提示": ['id', 'change_psw2-error'],
            "修改密码提交": ['id', 'submit_change_password'],
            "修改密码取消": ['css', '#now_change_password > div:nth-child(4) > div > input.btn.btn-primary.cancel-change'],
            "邮件发送成功": ['id', 'email_send_sucess'],
            "修改密码x": ['css', '#layui-layer1 > span > a'],
            "退出": ['css', '#hover-drop > ul > li:nth-child(7) > a'],
            "修改密码提示": ['css', '#layui-layer1 > div.layui-layer-content'],

        }
    page_texts= [
            '验证邮件已发送到您的邮箱',
            '修改密码成功',
    ]
    def lognin(self):
        #登录方法
        url = config.getConfig('url')
        username = config.getConfig('username')
        password = config.getConfig('password')
        self.send_keys('账号输入框', username)
        self.send_keys("密码输入框", password)
        self.click("登录按钮")

        self.move('个人资料入口')
        self.click('个人资料')
        self.open(url+'dashboard/security/')

    def input(self):
        #输入密码
        new_pwd = random.randint(100000, 999999)
        password = config.getConfig('password')
        self.click('重置密码')
        self.send_keys('原密码输入框', password)
        self.send_keys('新密码', new_pwd)
        self.send_keys('确认密码输入框', new_pwd)
        self.click('修改密码提交')
        success = self.text('修改密码提示')

        if success == self.page_texts[1]:
            config.writeConfig("password", new_pwd)
            return True
        else:
            return False






