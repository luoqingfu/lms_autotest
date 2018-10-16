from common.drive import Driver
from common.logger import Logging
from page_obj.lms_longin.lms_login import LmsLogin
from testCase.myunittest import myunittest

logger = Logging("LmsLoginTest").getlog()
class LmsLoginTest(myunittest):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.lmslogin = LmsLogin(driver)
        self.lmslogin.open(self.url)
        self.AssertionError = []

    def tearDown(self):
        self.lmslogin.quit()
        self.assertEqual([], self.AssertionError)
    def test_login_1(self):
        error_text = self.lmslogin.lms_login_test()
        print(error_text)
        if error_text == '密码错误' or error_text == '邮箱或手机号码格式有误':
            logger.error('登录用例错误')
            self.AssertionError.append("登录用例错误")
        else:
            logger.info('登录用例通过')

