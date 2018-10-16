from common.drive import Driver
from common.logger import Logging
from page_obj.persion_data.data_set import dataSet
from testCase.myunittest import myunittest

logger = Logging('dataSetT').getlog()
class dataSetT(myunittest):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.dataSet = dataSet(driver)
        self.dataSet.open(self.url)
        self.AssertionError = []
    def tearDown(self):
        self.dataSet.quit()
        self.assertEqual([], self.AssertionError)

    #修改用户资料测试

    def test_edit(self):
        self.dataSet.lognin()
        tests = self.dataSet.add_data()

        if str(tests[0]) == '我是呢称' and tests[1] != None:
            logger.info("修改信息成功")
        else:
            logger.error("修改信息失败")
            self.AssertionError.append("修改信息失败")

