from common.drive import Driver
from common.logger import Logging
from page_obj.pm.per_pm import perpmLogin
from page_obj.pm.register import perpmRegister

from testCase.myunittest import myunittest

logger = Logging("pmLoginTest").getlog()
class perpmLoginTest(myunittest):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.perpmRegister = perpmRegister(driver)
        self.perpmRegister.open('https://beta.eliteu.cn/')
        self.AssertionError = []

    def tearDown(self):
        self.perpmRegister.quit()
        self.assertEqual([], self.AssertionError)
    def test_login_1(self):
        #self.perpmRegister.cli()
        for i in range(len(self.perpmRegister.page_texts)):
            error_text = self.perpmRegister.per_login_test(i)
            print(error_text)
            if error_text != '邮箱或手机号码格式有误':
                logger.info('登录用例成功')

            else:
                logger.info('登录用例错误')
                self.AssertionError.append("登录用例错误")
