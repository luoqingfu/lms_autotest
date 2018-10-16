from common.drive import Driver
from common.logger import Logging
from page_obj.app_download.app_down import app_d
from testCase.myunittest import myunittest

logger = Logging('app_t').getlog()
class app_t(myunittest):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.app_d = app_d(driver)
        self.app_d.open(self.url)
        self.AssertionError = []
    def tearDown(self):
        self.app_d.quit()
        self.assertEqual([], self.AssertionError)
    def test_1texts(self):
        self.app_d.lognin()
        logger.info('app下载页面文本验证开始')
        h_texts = self.app_d.page_texts
        print(h_texts)
        reality_texts = self.app_d.texts()
        print(reality_texts)
        for (hope_texts, reality) in zip(h_texts, reality_texts):
            logger.info('对比开始')
            try:
                self.assertEqual(hope_texts, reality)
                logger.info("实际结果：{}，预期结果:{}".format(hope_texts, reality))
            except Exception as e:
                logger.error("**用例执行失败** %s" % e)
                self.AssertionError.append(e)

    def test_hascontian(self):
        self.app_d.lognin()
        logger.info('移动到立即下载')
        if self.app_d.move_to_e() == True:
            logger.info('正确移动到立即下载')
        else:
            logger.error('移动到立即下载用例失败')
            self.AssertionError.append('移动到立即下载失败')
