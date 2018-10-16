from common.drive import Driver
from common.logger import Logging
from page_obj.persion_data.change_pwd import change_pwd
from testCase.myunittest import  myunittest

logger = Logging('change_pwd_t').getlog()
class change_pwd_t(myunittest):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.change_pwd = change_pwd(driver)
        self.change_pwd.open(self.url)
        self.AssertionError = []
    def tearDown(self):
        self.change_pwd.quit()
        self.assertEqual([], self.AssertionError)
    def test_1changePwd(self):
        self.change_pwd.lognin()
        check = self.change_pwd.input()
        if check == True:
            logger.info('修改密码成功')
        else:
            self.AssertionError.append('修改密码功能错误')

