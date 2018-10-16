from common.drive import Driver
from common.logger import Logging
from page_obj.study_course.study_course import studyCourse
from testCase.myunittest import myunittest

logger = Logging('studuCourseT').getlog()
class studuCourseT(myunittest):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.studyCourse = studyCourse(driver)
        self.studyCourse.open(self.url)
        self.AssertionError = []
    def tearDown(self):
        self.studyCourse.quit()
        self.assertEqual([], self.AssertionError)
    def test_1choice_course(self):
        self.studyCourse.choice_course()
        check = self.studyCourse.write_comment()
        for check, check1 in zip(check[0], check[1]):
            try:
                self.assertEqual(check, check1)
                logger.info("实际文本：{}，预期文本：{}".format(check, check1))

            except  Exception as e:
                logger.error("********用例执行错误*********%s" % e)
                self.AssertionError.append("实际文本：{}，预期文本：{}".format(check, check1))

    def test_2watch_video(self):
        check = self.studyCourse.video()
        if check != '0:00 ':
            logger.info('播放按钮正常工作')
        else:
            logger.info('播放按钮异常')
            self.AssertionError.append('播放按钮异常')

