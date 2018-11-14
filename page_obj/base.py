import time


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

import readConfig

from common.logger import Logging
config = readConfig.ReadConfig()
logger = Logging("Page").getlog()
class Page():
    #初始化
    def __init__(self, driver):
        self.driver = driver
        self.config_element = {}
        self.time = float(config.getConfig("element_wait"))
        self.implicit_wait = float(config.getConfig("implicit_wait"))
    #通用的方法封装
    #单个元素定位
    def find_element(self, element):
        """单个元素定位"""
        try:
            el = self.config_element[element]
            type = el[0]
            value = el[1]
            if type == "ID" or type == "id" or type == "Id" or type == 'iD':
                try:
                    find_element = self.driver.find_element_by_id(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素ID为：{}@".format(value))
                    raise e
            elif type == "NAME" or type == "name" or type == "Name":
                try:
                    find_element = self.driver.find_element_by_name(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素NAME为：{}的元素@".format(value))
                    raise e
            elif type == "CLASSNAME" or type == "classname" or type == "ClassName":
                try:
                    find_element = self.driver.find_element_by_class_name(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素CLASSNAME为：{}的元素@".format(value))
                    raise e
            elif type == "TAGNAME" or type == "tagname" or type == "TagName":
                try:
                    find_element = self.driver.find_element_by_tag_name(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素TAGNAME为：{}的元素@".format(value))
                    raise e
            elif type == "LINKTEXT" or type == "linktext" or type == "LinkText":
                try:
                    find_element = self.driver.find_element_by_link_text(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素LINKTEXT为：{}的元素@".format(value))
                    raise e
            elif type == "PARTIALLINKTEXT" or type == "partiallinktext" or type == "PartialLinkText":
                try:
                    find_element = self.driver.find_element_by_partial_link_text(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素PARTIALLINKTEXT为：{}的元素@".format(value))
                    raise e
            elif type == "XPATH" or type == "xpath" or type == "XPath":
                try:
                    find_element = self.driver.find_element_by_xpath(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素XPATH为：{}的元素@".format(value))
                    raise e
            elif type == "CSS" or type == "css" or type == "Css":
                try:
                    find_element = self.driver.find_element_by_css_selector(value)
                    return find_element
                except Exception as e:
                    logger.error("@未发现元素CSS为：{}的元素@".format(value))
                    logger.error(e)
                    raise e
            else:
                error = "@{}模块下{}元素类型参数错误！@".format(element)
                logger.error(error)

        except KeyError as e:
            logger.error("@加载{}模块{}元素不匹配@".format(element))
            logger.error(e)
            raise e

    #多元素定位
    def find_elements(self,elements):
        """多元素定位"""
        try:
            el = self.config_element[elements]
            type = el[0]
            value = el[1]
            if type == "ID" or type == "id" or type == "Id":
                try:
                    find_element = self.driver.find_elements_by_id(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素ID为：{}@".format(value))
                    raise e
            elif type == "NAME" or type == "name" or type == "Name":
                try:
                    find_element = self.driver.find_elements_by_name(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素NAME为：{}的元素@".format(value))
                    raise e
            elif type == "CLASSNAME" or type == "classname" or type == "ClassName":
                try:
                    find_element = self.driver.find_elements_by_class_name(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素CLASSNAME为：{}的元素@".format(value))
                    raise e
            elif type == "TAGNAME" or type == "tagname" or type == "TagName":
                try:
                    find_element = self.driver.find_elements_by_tag_name(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素TAGNAME为：{}的元素@".format(value))
                    raise e
            elif type == "LINKTEXT" or type == "linktext" or type == "LinkText":
                try:
                    find_element = self.driver.find_elements_by_link_text(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素LINKTEXT为：{}的元素@".format(value))
                    raise e
            elif type == "PARTIALLINKTEXT" or type == "partiallinktext" or type == "PartialLinkText":
                try:
                    find_element = self.driver.find_elements_by_partial_link_text(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素PARTIALLINKTEXT为：{}的元素@".format(value))
                    raise e
            elif type == "XPATH" or type == "xpath" or type == "XPath":
                try:
                    find_element = self.driver.find_elements_by_xpath(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素XPATH为：{}的元素@".format(value))
                    raise e
            elif type == "CSS" or type == "css" or type == "Css":
                try:
                    find_element = self.driver.find_elements_by_css_selector(value)
                    return find_element
                except Exception as e:
                    logger.error("@未发现元素CSS为：{}的元素@".format(value))
                    logger.error(e)
                    raise e
            else:
                error = "@{}模块下{}元素类型参数错误！@".format(elements)
                logger.error(error)

        except KeyError as e:
            logger.error("@加载{}模块{}元素不匹配@".format(elements))
            logger.error(e)
            raise e

    #点击事件
    def click(self, element):
        """点击事件"""

        el = self.find_element(element)
        el.click()
        self.wait_time(1)


    #获取元素文本信息
    def text(self, element):
        """获取元素文本信息"""
        text = self.find_element(element).text

        self.wait_time(0.1)
        return text

    #获取当前页面的URL
    def get_url(self):
        """获取当前页面的URL"""
        return self.driver.current_url

    # 获取当前页面的title
    def get_title(self):
        """获取当前页面的title"""
        self.wait_time(0.5)
        title = self.driver.title
        logger.info("获取页面的title : %s"  %title)
        return  title

    #清空输入框，然后输入VALUE
    def send_keys(self, element, value):
        """清空输入框，然后输入VALUE"""
        self.wait_time(0.8)
        self.find_element(element).clear()
        self.find_element(element).send_keys(value)

    def send_keys_noclear(self,element, value):
        """清空输入框，然后输入VALUE"""
        self.wait_time(0.8)
        #self.find_element(page, element).clear()
        self.find_element( element).send_keys(value)


    # 下拉选择框
    def select(self,element, index):
        """下拉选择框"""
        Select(self.find_element( element)).select_by_index(index)


    #内嵌框架进行切换
    def iframe(self,element):
        """内嵌框架进行切换"""
        self.wait_time(1)
        self.driver.switch_to.frame(self.find_element(element))

    #鼠标事件
    def action(self):
        """鼠标事件"""
        self.wait_time(1)
        action = ActionChains(self.driver)
        return action

    #鼠标悬停
    def move(self, element):
        """鼠标悬停"""
        try:
            el = self.find_element(element)
            self.wait_time(0.5)
            self.action().move_to_element(el).perform()
        except Exception as e:
            logger.error("鼠标没有能正常悬停在的 {} 上".format( element))
            logger.error(e)
        self.wait_time(0.5)

    # 根据元素属性获取元素值
    def element_type_value(self, element, name="placeholder"):
        """根据元素属性获取元素值"""
        attribute = self.find_element(element).get_attribute(name)
        self.wait_time(0.5)
        return  attribute

    def element_type_input(self,element, name="value"):
        """根据元素属性获取输入值"""
        attribute = self.find_element(element).get_attribute(name)
        self.wait_time(0.5)
        return  attribute


    """对浏览器的一些操作--------------------------------------"""
    #打开网页
    def open(self,url):
        """打开网页"""
        self.driver.get(url)
        logger.info("浏览器中输入域名：%s" %url)

    #关闭当前页面
    def close(self):
        """关闭当前网页"""
        self.driver.close()
        logger.info("关闭当前页面")

    #关闭浏览器
    def quit(self):
        """关闭浏览器"""
        self.driver.quit()
        logger.info("关闭浏览器")

    #强制等待元素加载时间
    def wait_time(self, wait_time):
        """强制等待元素加载时间"""
        time.sleep(wait_time)

    #浏览器窗口定位切换
    def window(self, page='new_page'):
        """浏览器窗口定位切换"""
        handles = self.driver.window_handles
        lens = len(handles)
        if page == "new_page":
            if lens != 1:
                self.wait_time(0.5)
                self.driver.switch_to.window(handles[-1])
            else:
                self.wait_time(0.5)
                self.driver.switch_to.window(handles[0])
        elif page == "superior_page":
            self.wait_time(0.5)
            self.driver.switch_to.window(handles[-2])
        else:
            logger.error("@切换窗口参数错误@")
        self.wait_time(1)

    #页面 后退：-1 ，刷新当前页：0 ，前进：1
    def browser_page_handle(self,type ="-1"):
        """页面 后退：-1 ，刷新当前页：0 ，前进：1"""
        if type == "-1":
            self.wait_time(0.5)
            self.driver.back()
        elif type == "0":
            self.wait_time(0.5)
            self.driver.refresh()
        elif  type == "1":
            self.wait_time(0.5)
            self.driver.forward()
        else:
            logger.error("页面前进后退，操作参数错误！")
        self.wait_time(1)

    #调节浏览器窗口大小
    def window_sizi(self, width=None, height=None):
        """调节浏览器窗口大小"""
        self.wait_time(0.3)
        if width == None and height == None:
            self.driver.maximize_window()
        else:
            self.driver.set_window_size(width, height)


    # 通过javascript操作页面
    def javascript(self, js):
        """通过javascript操作页面"""
        try:
            self.driver.execute_script(js)
        except Exception as e:
            logger.error("@JS加载错误:%s@" % e)


    # 调节浏览器滚动条
    def page_location(self,down = 0,right = 0):
        """调节浏览器滚动条"""
        if str.isdigit(str(down)) and str.isdigit(str(right)):
            size = "window.scrollTo({},{})".format(down, right)
        else:
            logger.error("@加载浏览器的滚动条位置参数{}{}不是数字！@".format(down, right))
        self.javascript(size)
        self.wait_time(1)
    """保存图片"""
    # def get_windows_img(self,Fail=""):
    #     """
    #     在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
    #     """
    #     file_path = os.path.dirname(os.path.abspath('.')) + '/report/image/'
    #     rq = time.strftime('%m%d%H%M', time.localtime(time.time()))
    #     screen_name = file_path + rq +Fail+ '.png'
    #     try:
    #         self.wait_time(1)
    #         self.driver.get_screenshot_as_file(screen_name)
    #         logger.info("页面截图保存在 :/report/image/")
    #     except NameError as e:
    #         logger.error("@页面截图保存发生错误! %s@" % e)
    """对元素的位置进行操作"""
    # def get_location(self,page,element):
    #     list = []
    #     el = self.find_element(page,element)
    #     location  = el.location
    #     list.append(location)
    #     size = el.size
    #     list.append(size)
    #     return list
    #
    #
    # def get_relative_location(self,elementA,elementB):
    #     locationA = self.get_location(*elementA)
    #     xA = locationA[0]["x"]
    #     yA = locationA[0]["y"]
    #     heightA = locationA[1]["height"]
    #     widthA = locationA[1]["width"]
    #     locationB = self.get_location(*elementB)
    #     xB = locationB[0]["x"]
    #     yB = locationB[0]["y"]
    #     heightB = locationB[1]["height"]
    #     widthB = locationB[1]["width"]
    #     list=  []
    #     zuo = xB - xA
    #     shang = yB  - yA
    #     you = (widthB+xB)-(widthA+xA)
    #     xia = (heightA+yA)- (heightB+yB)
    #     list.append(zuo)
    #     list.append(shang)
    #     list.append(you)
    #     list.append(xia)
    #     return list
    """对元素的判断返回  True,False--------------------------------------"""
    #判断元素是否可见
    def is_displayed(self,element):
        """判断元素是否可见"""
        dis = self.find_element(element).is_displayed()
        logger.info("{}元素可见性为：{}".format(element, dis))
        return dis

    #判断元素是否存在
    def isElementExist(self, element,time=1):
        """判断元素是否存在"""
        try:
            self.driver.implicitly_wait(time)
            el = config_element[element]
            type = el[0]
            value = el[1]
            if type == "ID" or type == "id" or type == "Id":
                    find_element = self.driver.find_element_by_id(value)
            elif type == "NAME" or type == "name" or type == "Name":
                    find_element = self.driver.find_element_by_name(value)
            elif type == "CLASSNAME" or type == "classname" or type == "ClassName":
                    find_element = self.driver.find_element_by_class_name(value)
            elif type == "TAGNAME" or type == "tagname" or type == "TagName":
                    find_element = self.driver.find_element_by_tag_name(value)
            elif type == "LINKTEXT" or type == "linktext" or type == "LinkText":
                    find_element = self.driver.find_element_by_link_text(value)
            elif type == "PARTIALLINKTEXT" or type == "partiallinktext" or type == "PartialLinkText":
                    find_element = self.driver.find_element_by_partial_link_text(value)
            elif type == "XPATH" or type == "xpath" or type == "XPath":
                    find_element = self.driver.find_element_by_xpath(value)
            elif type == "CSS" or type == "css" or type == "Css":
                    find_element = self.driver.find_element_by_css_selector(value)
            return True
        except:
            self.driver.implicitly_wait(time+10)
            return False

    #判断元素是否为灰化状态
    def isEnabled(self,element):
        """判断元素是否为灰化状态"""
        enabled = self.find_element(element).is_enabled()
        logger.info("{}元素灰化状态：{}".format(element,enabled))
        return enabled

    #点选框是否为选中状态
    def is_select(self,element):
        """点选框是否为选中状态"""
        select = self.find_element(element).is_selected()
        logger.info("{}元素是否为点选状态：{}".format(element, select))
        return select

    def check_url(self, now_url, target_url, fun):
        """对比url选取最后一个一个/分隔内容"""
        now_url = now_url.split('/')
        target_url = target_url.split('/')

        if now_url[-1] == target_url[-1]:
            logger.info('%s btn is good' % fun)
            return True
        else:
            logger.error('%s btn is error' % fun)
            #logger.info('%s btn is error' % fun)
            return False


    def check_string(self, now_string, real_string):
        try:
            assert now_string == real_string
            logger.info("实际文本：{}，预期文本：{}".format(real_string, now_string))
        except:
            logger.info('%s 实际文本' % now_string)
    def new_window(self):
        """判断是否有新窗口打开"""
        all_handle = self.driver.window_handles
        if len(all_handle) > 1:
            logger.info("新窗口已打开")

        else:
            logger.info("没有新窗口打开")



    def window_to_old(self, page='old_page', old = 0):
        """该方法的前提是默认打开了新窗口"""
        handles = self.driver.window_handles
        lens = len(handles)
        if page == "old_page":
            if lens != 1:
                self.wait_time(0.5)
                self.driver.switch_to.window(handles[old])
            else:
                self.wait_time(0.5)
                self.driver.switch_to.window(handles[old])

        else:
            logger.error("@切换窗口参数错误@")
        self.wait_time(1)
    def alert(self, op):
        """警告框处理,1=确认，2=取消"""
        if op == 1:
            self.driver.switch_to.alert().accept()
        elif op == 2:
            self.driver.switch_to.alert().dismiss()
        else:
            logger.info("弹出框参数错误")
