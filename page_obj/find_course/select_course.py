from time import sleep

from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig


logger = Logging('selectCourse').getlog()
config = ReadConfig()
class selectCourse(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self.config_element = {
            "find_course": ["css", "#bs-example-navbar-collapse-1 > ul:nth-child(1) > li.all-discover-classify > a"],
            "选择一个课程": ["css", 'h3.course-name>a'],
            "全文": ["css",
                   'body > div:nth-child(11) > div > div.col-md-9 > div.panel.panel-default.course-detail > div > div.content > p > span'],
            "收起": ['css',
                   'body > div:nth-child(11) > div > div.col-md-9 > div.panel.panel-default.course-detail > div > div.content > div.more > p:nth-child(2) > span'],
            "内容": ['css',
                   'body > div:nth-child(11) > div > div.col-md-9 > div.panel.panel-default.course-detail > div > div.content > p'],
            "教授": ['css', '#professor > div > div > div.title > div > h2'],
            "课程大纲": ['id', 'curriculum-outline-tab'],
            "课程大纲_a": ['css', '#curriculum-outline > div'],
            "助教": ['id', 'course-assistant-tab'],
            "评价": ['id', 'comment-tab'],
            "评价_a": ['css',
                     '#comment > div.panel.panel-default.panel-comment > div > div.panel-left > div > p:nth-child(1)'],
            "免费试听": ['id', 'free_listen_for_login'],
            "加入课程": ['css',
                     'body > div:nth-child(11) > div > div.col-md-9 > div.panel.panel-default.course-detail > div > div.content > div.addenda.clearfix > div.text-right.fr > a.btn.btn-primary.loading.add_to_cart'],
            "进入课程": ['css',
                     'body > div:nth-child(11) > div > div.col-md-9 > div.panel.panel-default.course-detail > div > div.content > div.addenda.clearfix > div.text-right.fr > a'],
            "即将开课": ['css',
                     'body > div:nth-child(11) > div > div.col-md-9 > div.panel.panel-default.course-detail > div > div.content > div.addenda.clearfix > div.text-right.fr > a'],
            "结束试听": ['css',
                     'body > div:nth-child(11) > div > div.col-md-9 > div.panel.panel-default.course-detail > div > div.content > div.addenda.clearfix > div.text-right.fr > a.btn.btn-info.add_to_cart'],
            "账号输入框": ["id", "login_user_email"],
            "密码输入框": ['id', "login_password"],
            "登录按钮": ['css', "body > div.company-login.login01 > div > div.login-panel-body > form > div.form-group.no-margin-bot > div > button"],
            "课程更新信息": ["id", "msg-content-0"],
            "显示": ["css", 'button.toggle-visibility-button'],
            "隐藏": ["css", "button.toggle-visibility-button"],
            "第一章": ['css', '#main > div > div.info-wrapper > section.handouts > ul:nth-child(2) > li > a'],
        }
    def login(self):
        #通用的登录方法
        username = config.getConfig('username')
        password = config.getConfig('password')
        self.send_keys("账号输入框", username)
        self.send_keys("密码输入框", password)
        self.click("登录按钮")
    def select_a(self):

        #选择课程
        list = []
        self.login()
        self.click('find_course')
        coursename = self.find_elements('选择一个课程')
        coursename[0].click()
        self.new_window()
        self.window()
        url = self.get_url()
        print(url)
        contion = self.text('内容')
        #print(contion)
        self.click('全文')
        a_contion = self.text('内容')
        #print(a_contion)

        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        sleep(2)
        self.click('收起')
        l_contion = self.text('内容')
        #print(l_contion)
        self.click('课程大纲')
        list.append(self.text('课程大纲_a'))
        self.click('助教')
        self.click('评价')
        list.append(self.text('评价_a'))
        return contion, a_contion, l_contion, list

    def check_func(self):
        self.login()
        self.click('find_course')
        coursename = self.find_elements('选择一个课程')
        coursename[0].click()

        self.new_window()
        self.window()
        url = self.get_url()
        print(url)

        self.click('免费试听')
        self.new_window()
        self.window()
        url = self.get_url()
        print(url)
        check1 = self.check_url(self.get_url(), Page_Text['lms_course'][0], '免费试听')
        self.browser_page_handle()
        self.click('加入课程')
        check2 = self.check_url(self.get_url(), Page_Text['lms_course'][1], '加入课程')
        return check1, check2


    def check_free30(self):
        list = []
        self.login()
        self.click('find_course')

        coursename = self.find_elements('选择一个课程')
        #xu
        for n in range(len(coursename)):
            print(n)
            coursename = self.find_elements('选择一个课程')
            coursename[n].click()
            self.new_window()
            self.window()
            try:
                self.text('免费试听')
                self.click('免费试听')
                msg = self.text("课程更新信息")
                self.click("隐藏")
                msg1 = self.text("课程更新信息")
                list.append(msg)
                list.append(msg1)
                self.click( "第一章")
                self.new_window()

            except Exception as e:
                logger.info('没有进入课程列表')
            try:
                self.text('即将开课')

                msg = self.text("课程更新信息")
                self.click("隐藏")
                msg1 = self.text("课程更新信息")
                list.append(msg)
                list.append(msg1)
                self.click("第一章")
                self.new_window()

            except Exception as e:
                logger.info('没有进入即将开课')
            try:
                self.text('结束试听')
                self.click('结束试听')
                msg = self.text("课程更新信息")
                self.click("隐藏")
                msg1 = self.text("课程更新信息")
                list.append(msg)
                list.append(msg1)
                self.click("第一章")
                self.new_window()


            except Exception as e:
                logger.info('没有进入结束试听')
            try:
                self.text('加入课程')
                self.click('加入课程')
                msg = self.text("课程更新信息")
                self.click("隐藏")
                msg1 = self.text("课程更新信息")
                list.append(msg)
                list.append(msg1)
                self.click("第一章")
                self.new_window()


            except Exception as e:
                logger.info('没有进入加入课程')

            self.window_to_old('old_page', 0)



