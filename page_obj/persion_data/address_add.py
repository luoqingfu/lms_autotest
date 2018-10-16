from common.function import Excel
from common.logger import Logging
from page_obj.base import Page
from readConfig import ReadConfig



logger = Logging('addressAdd').getlog()
config = ReadConfig()
class addressAdd(Page):
    def __init__(self,driver):
        Page.__init__(self,driver)
        self.config_element = {
            "地址管理": ['css', '#myTabs > li:nth-child(3) > a'],
            "个人资料入口": ['css', '#hover-drop > a > img'],
            "个人资料": ['css', '#hover-drop > ul > li:nth-child(2) > a'],
            "添加新地址": ['css', '#tab3 > div > div > div > button'],
            "收件人姓名": ['id', 'consignee'],
            "收件人手机号码": ['id', 'consignee_tel'],
            "选择省": ['id', 'province'],
            "广东": ['css', '#province > option:nth-child(20)'],
            "选择市": ['id', 'city'],
            "深圳": ['css', '#city > option:nth-child(4)'],
            "选择区": ['id', 'district'],
            "南山": ['css', '#district > option:nth-child(4)'],
            "提交": ["id", 'btn-submit'],
            "右上角x": ["css", 'body > div:nth-child(11) > div.mask.mask_address > div > div.popup-head > span.close.fa.fa-times'],
            "地址错误信息": ['id', 'consignee-error'],
            "手机号码错误信息": ['id', 'consignee_tel-error'],
            "详细地址错误信息": ['id', 'address-error'],
            "详细地址": ['id', 'address'],
            "编辑地址": ['css', '#tab3 > div > div > div:nth-child(5) > div > span.right-btm > span'],
            "地址信息": ['css', '#tab3 > div > div > div:nth-child(5) > div > div:nth-child(1) > div > p'],
            "地址div": ['css', 'div.section'],
            "设置为默认": ['css', 'span.link.set-default'],
            "默认": ['css', '#tab3 > div > div > div:nth-child(5) > p > span:nth-child(1)'],
            "忘记密码": ['id', 'forget_password'],
            "验证码登录": ['css', 'body > div.company-login.login01 > div > div.login-panel-body > form > div.tips > div > a.pull-right.code-btn'],
            "账号密码登录": ['id', 'accout-login'],
            "账号输入框": ["id", "login_user_email"],
            "密码输入框": ['id', "login_password"],
            "登录按钮": ['css', "body > div.company-login.login01 > div > div.login-panel-body > form > div.form-group.no-margin-bot > div > button"],

        }
    def get_excel_data(self, dataname, row=2):
        data = Excel(dataname)
        return data.read_excel(row)
    def lognin(self):
        #登录方法
        username = config.getConfig('username')
        password = config.getConfig('password')
        self.send_keys('账号输入框', username)
        self.send_keys("密码输入框", password)
        self.click("登录按钮")
        self.move('个人资料入口')
        self.click('个人资料')
        self.click('地址管理')

    def address_add(self):
        #添加地址，返回提示信息
        list = []
        datas = self.get_excel_data('address/address', 1)
        for n in range(len(datas)):

            self.click('添加新地址')
            self.send_keys('收件人姓名', datas[n]['address'])
            self.send_keys('收件人手机号码', datas[n]['tel'])
            self.click('选择省')
            self.click('广东')
            self.click('选择市')
            self.click('深圳')
            self.click('选择区')
            self.click('南山')
            self.send_keys('详细地址', datas[n]['d_address'])
            self.click('提交')
            #print(self.is_displayed('personal_data', '地址错误信息'))
            if self.isElementExist('地址错误信息') == True:
                logger.info('获取地址错误信息正确')
                list.append(self.text('地址错误信息'))
            else:
                list.append('')
                logger.info('没有获取地址错误信息')
            if self.isElementExist('手机号码错误信息') == True:
                logger.info('获取手机号码错误信息正确')
                list.append(self.text('手机号码错误信息'))
            else:
                list.append('')
                logger.info('没有获取手机号码错误信息信息')
            if self.isElementExist('详细地址错误信息') == True:
                logger.info('获取详细地址错误信息正确')
                list.append(self.text('详细地址错误信息'))
            else:
                list.append('')
                logger.info('没有获取详细地址错误信息')
            if self.isElementExist('地址错误信息') or \
                self.isElementExist('手机号码错误信息') or \
                self.isElementExist('详细地址错误信息') == True:
                self.click('右上角x')
            else:
                logger.info('成功添加信息')

        return list

    def address_edit(self):
        #修改收件人地址
        print(self.isElementExist('编辑地址'))
        if self.isElementExist('编辑地址') == True:
            self.click('编辑地址')
            self.send_keys('收件人姓名', '我是收件人姓名')
            self.click('提交')
        else:
            logger.error('编辑地址不存在')
        address_msg = self.text('地址信息')
        return address_msg

    def address_default(self):
        #修改默认地址
        self.click('添加新地址')
        self.send_keys('收件人姓名', '我是新建内容')
        self.send_keys('收件人手机号码', '13226349780')
        self.click('选择省')
        self.click('广东')
        self.click('选择市')
        self.click('深圳')
        self.click('选择区')
        self.click('南山')
        self.send_keys('详细地址', '我不是天河北路')
        self.click('提交')
        el = self.find_elements('地址div')
        self.action().move_to_element(el[1]).perform()
        # el_default = self.find_elements('personal_data', '设置为默认')
        # print(el_default[1], '11111111111111111111')
        # #self.wait_time(3)
        # el_default[1].click()
        self.click('设置为默认')
        self.wait_time(3)
        if self.text('默认') == '我是新建内容' :
            logger.info('设置默认成功')
            return True
        else:
            return False




