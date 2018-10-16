from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig




logger = Logging('find_course').getlog()
config = ReadConfig()
moneyis = 198.00
class study_centre(Page):
    def __init__(self,driver):
        Page.__init__(self,driver)
        self.config_element = {
            "选择一个课程": ['css', '#page1 > div > div > div > div.course-aside.panel-md > div.course-about > h3 > a'],
            "已完成": ['css', '#myTabs > li:nth-child(2) > a'],
            "助教": ['xpath', '//*[@id="course_user_menu"]/a[3]'],
            "助教_已完成": ['css', '#myTabs > li:nth-child(2) > a'],
            "助教_已取消": ['xpath', '//*[@id="myTabs"]/li[3]'],
            "宝典": ['xpath', '//*[@id="course_user_menu"]/a[5]'],
            "宝典获取": ['id', 'tab1-tab'],
            "宝典支出": ['css', '#myTabs > li:nth-child(2)'],
            "转赠": ['css',
                   'body > div:nth-child(11) > div.container > div > div.stay-r > div > div.panel-body.relate > div.book-recharge > button'],
            "对方id": ['id', 'user_id'],
            "对方账号": ['id', 'phone_or_email'],
            "转赠宝典": ['id', 'max_score'],
            "转赠_关闭": ['css', 'body > div:nth-child(11) > div.mask > div > div.popup-head > span'],
            "宝典_确认": ['id', 'give_score'],
            "宝典_充值": ['css',
                      'body > div:nth-child(11) > div.container > div > div.stay-r > div > div.panel-body.relate > div.book-recharge > a'],
            "充值_确认": ['id', 'btn_subimit_coin'],
            "充值_数额": ['css',
                      'body > div:nth-child(11) > div > div.stay-r > div > div > div > div:nth-child(1) > div > div.panel-heading > p:nth-child(2) > span > span'],
            "充值宝典": ['css',
                     'body > div:nth-child(11) > div > div.stay-r > div > div > div > div:nth-child(1) > div > div.panel-body > div > span:nth-child(2)'],
            "总获得宝典": ['css',
                      'body > div:nth-child(11) > div > div.stay-r > div > div > div > div:nth-child(1) > div > div.panel-body > div > span:nth-child(6)'],
            "其他金额": ['id', 'coin_amount'],
            "申请开发票": ['css',
                      'body > div:nth-child(11) > div > div.stay-r > div > div > div > div:nth-child(9) > div.for-bill > div > input'],
            "申请开发票_l": ['css',
                        'body > div:nth-child(11) > div > div.stay-r > div > div > div > div:nth-child(9) > div.panel.panel-default.form-panle.text-left.triangle.ask-invoice-detail'],
            "账号输入框": ["id", "login_user_email"],
            "密码输入框": ['id', "login_password"],
            "登录按钮": ['css', "body > div.company-login.login01 > div > div.login-panel-body > form > div.form-group.no-margin-bot > div > button"],

        }
    page_texts = [
        "https://rk98tc.e-ducation.cn/dashboard/courses/learning/",
        'https://rk98tc.e-ducation.cn/dashboard/courses/finished/',
        'https://rk98tc.e-ducation.cn/dashboard/studentservice/pending',
        'https://rk98tc.e-ducation.cn/dashboard/studentservice/finished',
        'https://rk98tc.e-ducation.cn/dashboard/studentservice/canceled',
        'https://rk98tc.e-ducation.cn/dashboard/coingain/',
        'https://rk98tc.e-ducation.cn/dashboard/coincost/',
        'https://rk98tc.e-ducation.cn/finance/coin/',
        ]

    def login(self):
        """通用的登录方法"""
        username = config.getConfig('username')
        password = config.getConfig('password')
        self.send_keys('账号输入框', username)
        self.send_keys("密码输入框", password)
        self.click("登录按钮")

    def select_course(self):
        #验证我的课程
        self.login()
        #self.click('homepage', '选择一个课程')
        check1 = self.check_url(self.get_url(), self.page_texts[0], '课程_正在学习')
        self.click('已完成')
        check2 = self.check_url(self.get_url(), self.page_texts[1], '课程_已完成')

        return check1, check2
    def teaching_assistant(self):
        #助教功能测试功能不常用，只做点击测试
        self.login()
        self.click('助教')
        check1 = self.check_url(self.get_url(), self.page_texts[2], '助教_等待中')
        self.click('助教_已完成')
        check2 = self.check_url(self.get_url(), self.page_texts[3], '助教_已完成')
        self.click('助教_已取消')
        check3 = self.check_url(self.get_url(), self.page_texts[4], '助教_取消')

        return check1, check2, check3

    def book_value(self):
        #宝典功能测试
        username = config.getConfig('username')
        self.login()
        self.click('宝典')
        check1 = self.check_url(self.get_url(), self.page_texts[5], '宝典获取')
        self.click('宝典支出')
        check2 = self.check_url(self.get_url(), self.page_texts[6], '宝典支出')
        self.click('转赠')
        try:
            self.send_keys('对方id', username)
            self.send_keys('对方账号', username)
            self.send_keys('转赠宝典', username)
            self.click('宝典_确认')
            self.click('转赠_关闭')

        except Exception as e:
            logger.error('转赠功能错误')
            pass
        self.click('宝典_充值')
        check3 =self.check_url(self.get_url(), self.page_texts[7], '宝典充值')
        self.click('充值_确认')
        money = self.text('充值_数额')


        return check1, check2, check3, money
