from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig

logger = Logging('dataSet').getlog()
config =  ReadConfig()
img_path = '/Users/qfl/eliproject/Elite-live-autotest/lms/lms_function_test/testFile/image/timg.jpeg'
class dataSet(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
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
            "收件人姓名": ['id', 'consignee'],
            "收件人手机号码": ['id', 'consignee_tel'],
            "选择省": ['id', 'province'],
            "广东": ['css', '#province > option:nth-child(20)'],
            "选择市": ['id', 'city'],
            "深圳": ['css', '#city > option:nth-child(4)'],
            "选择区": ['id', 'district'],
            "南山": ['css', '#district > option:nth-child(4)'],
            "提交": ["id", 'btn-submit'],
            "右上角x": ["css",
                     'body > div:nth-child(11) > div.mask.mask_address > div > div.popup-head > span.close.fa.fa-times'],
            "地址错误信息": ['id', 'consignee-error'],
            "手机号码错误信息": ['id', 'consignee_tel-error'],
            "详细地址错误信息": ['id', 'address-error'],
            "详细地址": ['id', 'address'],
            "编辑地址": ['css', '#tab3 > div > div > div:nth-child(5) > div > span.right-btm > span'],
            "地址信息": ['css', '#tab3 > div > div > div:nth-child(5) > div > div:nth-child(1) > div > p'],
            "地址div": ['css', 'div.section'],
            "设置为默认": ['css', 'span.link.set-default'],
            "默认": ['css', '#tab3 > div > div > div:nth-child(5) > p > span:nth-child(1)'],
            "选择图片": ['id', 'chooseuserpic'],
            "昵称": ['id', 'nickname'],
            "最高学历": ['css', '#profile_form > div:nth-child(4) > div > div > span'],
            "博士学位": ['css', 'span.selecter-item'],
            "保存": ['id', 'save_user_info'],

        }
    def lognin(self):
        #登录方法
        username = config.getConfig('username')
        password = config.getConfig('password')
        self.send_keys('账号输入框', username)
        self.send_keys("密码输入框", password)
        self.click("登录按钮")
        self.move('个人资料入口')
        self.click('个人资料')
    def add_data(self):
        # el = self.find_element('data', '选择图片')
        # self.send_keys('data', '选择图片', '/Users/qfl/eliproject/Elite-live-autotest/lms/lms_function_test/testFile/image/timg.jpeg')
        # self.wait_time(4)
        self.send_keys('昵称', '我是呢称')
        self.click('最高学历')
        el = self.find_elements('博士学位')
        el[4].click()
        self.click('保存')
        list = []
        list.append(self.element_type_value('昵称', 'value'))
        #list.append(self.text('data', '昵称'))
        list.append(self.text('最高学历'))

        return list





