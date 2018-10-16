import random

from common.function import Random
from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig

logger = Logging('studyCourse').getlog()
config = ReadConfig()
class studyCourse(Page, Random):
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
            "发现课程": ['css', '#bs-example-navbar-collapse-1 > ul:nth-child(1) > li.all-discover-classify > a'],
            "课程": ['css', 'li.tab:nth-child(2) > a:nth-child(1)'],

            "笔记": ['css', '#content > div.aside-btn > div.note-btn.show-note-popup.ta-btn'],
            "咨询": ['id', 'add_new_consult'],
            "写评论": ['id', 'add_comment'],
            "评论tab": ['css', '#comment_tag>.btn.btn-default'],
            "评论内容": ['id', 'comment_content'],
            "评论提交": ['id', 'btn_submit'],

            "评论标签": ['css',
                     '#comment_list>.panel.panel-default.user-comment>.panel-body>.comment-body.clearfix>.content-label>.btn.btn-default'],
            "提交确认": ['css', '.layui-layer-btn0'],
            "播放按钮": ['css', '#video_6644eb6158544b8588565f40ada89750 > div.tc-wrapper > div > div.video-controls > div:nth-child(2) > div.vcr > button'],
            "视屏进度": ['css', '#video_6644eb6158544b8588565f40ada89750 > div.tc-wrapper > div > div.video-controls > div:nth-child(2) > div.vcr > div'],

        }

    def login(self):
        # 登录方法
        username = config.getConfig('username')
        password = config.getConfig('password')

        self.send_keys('账号输入框', username)
        self.send_keys("密码输入框", password)
        self.click("登录按钮")


    def choice_course(self):

        self.login()
        self.click('find_course')

        coursename = self.find_elements('选择一个课程')
        # xu
        for n in range(len(coursename)):
            print(n)
            coursename = self.find_elements('选择一个课程')
            coursename[n].click()
            self.new_window()
            self.window()

            try:
                join = self.text('进入课程')
                self.click('进入课程')
                self.new_window()
                self.window()
                self.wait_time(2)
                #self.click('study_course', '课程')
                course_url = self.element_type_value('课程', name="href")
                print(course_url)
                self.click('课程')
                if join == '进入课程':
                    break
            except Exception as e:
                logger.info('没有进入课程列表')
            self.window_to_old('old_page', 0)

    def click_three(self):
        self.click('助教')
        self.window()
        self.close()

    def write_comment(self):

        self.click('写评论')
        comment_num = self.find_elements('评论tab')

        list = []
        cha = ''
        run = len(comment_num) - random.randint(0, len(comment_num)-2)
        for n in range(run):
            comment_num[n].click()
            tab_name = comment_num[n].text
            list.append(tab_name)
            char = self.get_random_symbol()
            cha = cha + char
        self.send_keys('评论内容', cha)
        self.click('评论提交')
        self.click('提交确认')
        self.browser_page_handle()
        self.browser_page_handle()
        self.browser_page_handle(type='0')
        self.wait_time(2)
        self.click('评价')
        tab_comment = self.find_elements('评论标签')

        list1 = []
        for n in range(run):
            tab_name = tab_comment[n].text
            list1.append(tab_name)
        print(list)
        print(list1)
        return list, list1
    def video(self):

        self.choice_course()
        self.click('播放按钮')
        self.wait_time(4)
        #print('时间为', self.text('study_course', '视屏进度'))
        video_time = str(self.text('视屏进度'))
        #print(video_time.split('/')[0])
        return video_time.split('/')[0]












