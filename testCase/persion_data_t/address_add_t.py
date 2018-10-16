from common.drive import Driver
from common.logger import Logging
from page_obj.base import Page
from page_obj.persion_data.address_add import addressAdd
from testCase.myunittest import  myunittest

logger = Logging('address_add').getlog()
class address_add(myunittest, Page):
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        self.addressAdd = addressAdd(driver)
        self.addressAdd.open(self.url)
        self.AssertionError = []
    def tearDown(self):
        self.addressAdd.quit()
        self.assertEqual([], self.AssertionError)
    def test_1address(self):
        #添加地址测试
        self.addressAdd.lognin()
        real_texts = self.addressAdd.address_add()
        #print(real_texts, '########3')
        list = []
        hope_texts = self.get_excel_data('address/address', 1)
        for n in range(len(hope_texts)):
            list.append(hope_texts[n]['consignee-error'])
            list.append(hope_texts[n]['consignee_tel-error'])
            list.append(hope_texts[n]['address-error'])

        #print(list, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
        for (h_t, r_t) in zip(list, real_texts):
            logger.info('对比开始')
            try:
                self.assertEqual(h_t, r_t)
                logger.info("实际结果：{}，预期结果:{}".format(h_t, r_t))
            except Exception as e:
                logger.error("**用例执行失败** %s" % e)
                self.AssertionError.append(e)

    def test_2edit(self):
        #修改地址信息测试
        self.addressAdd.lognin()
        text = self.addressAdd.address_edit()
        self.wait_time(1)
        try:
            self.assertEqual(text, '我是收件人姓名')
            logger.info('修改地址用例通过')
        except Exception as e:
            logger.error('用例执行失败%s' % e)
            self.AssertionError.append(e)

    def test_3default(self):
        self.addressAdd.lognin()
        status = self.addressAdd.address_default() == False
        print(status)
        if status == True:
            logger.info('修改默认成功')
        elif status == False:
            self.AssertionError.append('修改默认失败')


