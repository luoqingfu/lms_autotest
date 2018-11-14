from common.drive import Driver
from common.logger import Logging
from page_obj.base import Page
from page_obj.pm.af import lmsAF
from testCase.myunittest import myunittest

logger = Logging("lmsAFtest").getlog()
class lmsAFtest(myunittest,Page):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.lmsAF =lmsAF(driver)
        self.lmsAF.open(self.url)
        self.AssertionError = []

    def tearDown(self):
        self.lmsAF.quit()
        self.assertEqual([], self.AssertionError)
    def test_1forget(self):
        #测试忘记密码功能
        self.lmsAF.cli()
        for i in range(len(self.lmsAF.page_texts)-3):
            check = self.lmsAF.forget_t(i+3)
            if check != '邮箱或手机号码格式有误':
                logger.info('忘记密码功能正常')
            else:
                self.AssertionError.append("登录用例错误")

    def test_2autcode(self):
        #测试验证码登录功能
        #print(111111111111111111111111111,range(len(self.lmsAF.page_texts) - 3):)
        self.lmsAF.cli2()
        for i in range(len(self.lmsAF.page_texts) - 3):
            check = self.lmsAF.authcode_t(i+3)
            print('错误信息{}:'.format(check))
            if check != '邮箱或手机号码格式有误':
                logger.info('验证码登录功能正常')
            else:
                logger.info('验证码登录功能异常')
                self.AssertionError.append('验证码登录用例错误')