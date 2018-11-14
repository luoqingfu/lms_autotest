from common.drive import Driver
from common.logger import Logging
from page_obj.base import Page
from page_obj.send.send_p import test_s

from testCase.myunittest import  myunittest

logger = Logging('send_test').getlog()
class send_test(myunittest, Page):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.test_s = test_s(driver)
        self.test_s.open('https://4xjhtu.beta.e-ducation.cn/live/1415/login')
        self.AssertionError = []
    def tearDown(self):
        self.test_s.quit()
        self.assertEqual([], self.AssertionError)
    def test_1address(self):
        self.test_s.login()
        self.test_s.send_msg()
