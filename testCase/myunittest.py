import unittest
from common.drive import Driver
from common.function import Excel
from page_obj.app_download.app_down import app_d
from page_obj.find_course.select_course import selectCourse
from page_obj.homepage.study_centre import study_centre

from page_obj.lms_longin.lms_login import LmsLogin
from page_obj.lms_longin.lms_login_fun import lmsLoginFun
from page_obj.persion_data.address_add import addressAdd
from page_obj.persion_data.change_pwd import change_pwd
from page_obj.persion_data.data_set import dataSet
from page_obj.persion_data.safe import safeEdit
from page_obj.study_course.study_course import studyCourse

from readConfig import ReadConfig


config = ReadConfig()


class myunittest(unittest.TestCase):
    """继承unnittest"""
    url = config.getConfig("url")
    browser = config.getConfig("browser")

    """获取EXCEL表数据"""
    def get_excel_data(self, dataname, row=2):
        data = Excel(dataname)
        return data.read_excel(row)
    """给EXCEL表插入数据"""
    def set_excel_data(self, dataname, datas, row=2):
        excel_data = Excel(dataname)
        excel_data.write_excel(datas, row)


