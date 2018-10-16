from time import sleep

from common.drive import Driver
from common.logger import Logging
from page_obj.homepage.study_centre import study_centre
from testCase.myunittest import myunittest

logger = Logging('homePageTest').getlog()
class homePageTest(myunittest):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.study_centre = study_centre(driver)
        self.study_centre.open(self.url)

        self.AssertionError = []

    def tearDown(self):
        self.study_centre.quit()
        self.assertEqual([], self.AssertionError)
    def test_1study_course(self):
        check = self.study_centre.select_course()

        if check[0] == True:
            logger.info('课程_正在学习is true')
        else:
            self.AssertionError.append('课程_正在学习is false')
        if check[1] == True:
            logger.info('课程_正在学习is true')
        else:
            self.AssertionError.append('课程_正在学习is false')

    def test_2teaching_assistant(self):
        check = self.study_centre.teaching_assistant()
        if check[0] == True:
            logger.info('助教_待服务is true')
        else:
            self.AssertionError.append('助教_待服务is false')
        if check[1] == True:
            logger.info('助教_已完成is true')
        else:
            self.AssertionError.append('助教_已完成is false')
        if check[2] == True:
            logger.info('助教_已取消is true')
        else:
            self.AssertionError.append('助教_已取消is false')

    def test_3valuablebook(self):
        moneyis = '198.00'
        check = self.study_centre.book_value()
        if check[0] == True:
            logger.info('宝典获取is true')
        else:
            self.AssertionError.append('宝典获取is false')
        if check[1] == True:
            logger.info('宝典支出is true')
        else:
            self.AssertionError.append('宝典支出is false')
        if check[2] == True:
            logger.info('宝典充值is true')
        else:
            self.AssertionError.append('宝典充值is false')

        if  check[3] == moneyis:
            logger.info('宝典充值金额is true')
        else:
            self.AssertionError.append('宝典充值金额is false')
