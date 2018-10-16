from common.drive import Driver
from common.logger import Logging
from page_obj.lms_longin.lms_login_fun import lmsLoginFun

from testCase.myunittest import myunittest


logger = Logging("lmsLoginFunt").getlog()
class lmsLoginFunt(myunittest):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.LmsLoginFun = lmsLoginFun(driver)
        self.LmsLoginFun.open(self.url)
        self.AssertionError = []

    def tearDown(self):
        self.LmsLoginFun.quit()
        self.assertEqual([], self.AssertionError)
    def test_1forget(self):
        #测试忘记密码功能
        check = self.LmsLoginFun.forget_t()
        if check == True:
            logger.info('忘记密码功能正常')
        else:
            self.AssertionError.append("登录用例错误")

    def test_2autcode(self):
        #测试验证码登录功能
        check = self.LmsLoginFun.authcode_t()
        if check == False:
            logger.info('验证码登录功能正常')
        else:
            logger.info('验证码登录功能异常')
            self.AssertionError.append('验证码登录用例错误')

    def test_3translate(self):
        #测试中英文切换功能
        check = self.LmsLoginFun.translate_t()
        #print(check)
        if check[0] == self.LmsLoginFun.page_texts[1] and check[1] == self.LmsLoginFun.page_texts[2]:
            logger.info('中英文切换功能正常')
        else:
            logger.error('中英文切换功能异常')
            self.AssertionError.append('中英文切换用例错误')
