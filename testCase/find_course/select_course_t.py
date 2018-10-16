from common.drive import Driver
from common.logger import Logging
from page_obj.base import Page
from page_obj.find_course.select_course import selectCourse

from testCase.myunittest import myunittest

logger = Logging('selectCourseT').getlog()
class selectCourseT(myunittest,Page):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.select_course = selectCourse(driver)
        self.select_course.open(self.url)
        self.AssertionError = []
    def tearDown(self):
        self.select_course.quit()
        self.assertEqual([], self.AssertionError)
    def test_1select(self):
        check = self.select_course.select_a()
        if check[0] == check[2]:
            logger.info('点开全文成功')
        else :
            self.AssertionError.append('点开全文失败')
        if check[3][0] != '' and check[3][1] != '':
            logger.info('授课老师，课程大纲，助教，评加功能通过')
        else:
            self.AssertionError.append('授课老师，课程大纲，助教，评鉴功能失败')
    def test_2fu(self):
        check = self.select_course.check_func()
        if check[0] == True:
            logger.info('试听功能通过')
        else:
            logger.info('试听功能fail')
            self.AssertionError.append('试听功能fail')
        if check[1] == True:
            logger.info('加入课程功能通过')
        else:
            logger.info('加入课程功能fail')
            self.AssertionError.append('加入课程功能fail')


    def test_3freee(self):
        self.select_course.check_free30()



