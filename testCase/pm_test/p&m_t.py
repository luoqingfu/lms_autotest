from common.drive import Driver
from common.logger import Logging
from page_obj.pm.pm import pmLogin

from testCase.myunittest import myunittest

logger = Logging("pmLoginTest").getlog()
class pmLoginTest(myunittest):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.pmLogin = pmLogin(driver)
        self.pmLogin.open(self.url)
        self.AssertionError = []

    def tearDown(self):
        self.pmLogin.quit()
        self.assertEqual([], self.AssertionError)
    def test_login_1(self):
        for i in range(len(self.pmLogin.page_texts)):
            error_text = self.pmLogin.lms_login_test(i)
            print(error_text)
            if error_text != '邮箱或手机号码格式有误':
                logger.info('登录用例成功')
                self.AssertionError.append("登录用例成功")
            else:
                logger.info('登录用例错误')
