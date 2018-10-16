from common.drive import Driver
from common.logger import Logging
from page_obj.base import Page
from page_obj.persion_data.safe import safeEdit
from testCase.myunittest import myunittest



logger = Logging('safe_e').getlog()
class safe_e(myunittest, Page):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.safeEdit = safeEdit(driver)
        self.safeEdit.open(self.url)
        self.AssertionError = []
    def tearDown(self):
        self.safeEdit.quit()
        self.assertEqual([], self.AssertionError)
    def test_1email(self):
    #测试邮箱修改
        self.safeEdit.lognin()
        check = self.safeEdit.edit_email_cancel()
        try:
            self.assertEqual(check, True)
            logger.info('取消按钮生效')
        except Exception as e:
            self.AssertionError.append(e)
        check1 = self.safeEdit.edit_email_commit()
        # print(Page_Text['safe'][0])
        # print(check1)
        try:

            self.assertEqual(check1, Page_Text['safe'][0])
            logger.info('发送邮件成功')
        except Exception as e:
            self.AssertionError.append(e)


    def test_2phone(self):
        #测试修改手机号码
        self.safeEdit.lognin()
        check = self.safeEdit.change_phone_cancel()
        try:
            self.assertEqual(check, True)
            logger.info('取消按钮成功')
        except Exception as e:
            self.AssertionError.append(e)
        check1 = self.safeEdit.change_phone_commit()
        print(check1)
        # try:
        #     self.assertEqual(check1, True)
        #     logger.info('修改密码成功')
        # except Exception as e:
        #     self.AssertionError.append(e)

