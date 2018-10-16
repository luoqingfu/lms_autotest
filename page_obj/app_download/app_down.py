from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig
logger = Logging('app_d').getlog()
config = ReadConfig()
class app_d(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self.config_element = {

                "app下载": ['css', '#bs-example-navbar-collapse-1 > ul:nth-child(1) > li:nth-child(4) > a'],
                "立即下载": ['css', 'body > div.app-download-banner > div.container > div.app-download-text > div > a'],
                "有效管理": ['css', 'body > div.container > div > div > ul > li:nth-child(1) > p:nth-child(3)'],
                "及时关注": ['css', 'body > div.container > div > div > ul > li:nth-child(2) > p:nth-child(3)'],
                "节奏自掌控": ['css', 'body > div.container > div > div > ul > li:nth-child(3) > p:nth-child(3)'],
                "随堂小测": ['css', 'body > div.container > div > div > ul > li:nth-child(4) > p:nth-child(3)'],
                "直播讲座": ['css', 'body > div.container > div > div > ul > li:nth-child(5) > p:nth-child(3)'],
                "生动体验": ['css', 'body > div.container > div > div > ul > li:nth-child(6) > p:nth-child(3)'],
                "图片": ['css', 'div.mytips:nth-child(1) > object:nth-child(1) > a:nth-child(1) > img:nth-child(1)'],
                "账号输入框": ["id", "login_user_email"],
                "密码输入框": ['id', "login_password"],
                "登录按钮": ['css', "body > div.company-login.login01 > div > div.login-panel-body > form > div.form-group.no-margin-bot > div > button"],

        }
    page_texts = [
                '课件视频一目了然，清楚了解学习进度',
                '随时关注课程内容更新，查找有用资源',
                '课程随时暂停快进回放，支持离线下载',
                '掌上完成习题考核，即时巩固学习效果',
                '多人实时学习，在线问卷、签到、回看',
                '黑板+音频+PPT在线实时培训',

    ]
    def lognin(self):
        #登录方法
        username = config.getConfig('username')
        password = config.getConfig('password')
        self.send_keys('账号输入框', username)
        self.send_keys("密码输入框", password)
        self.click("登录按钮")
        self.click('app下载')

    def texts(self):

        #文本验证
        list = []
        list.append(self.text('有效管理'))
        list.append(self.text('及时关注'))
        list.append(self.text('节奏自掌控'))
        list.append(self.text('随堂小测'))
        list.append(self.text('直播讲座'))
        list.append(self.text('生动体验'))
        return list

    def move_to_e(self):
        #移动到立即下载
        self.move('立即下载')
        return self.isElementExist( "图片")




