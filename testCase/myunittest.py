import unittest

from common.function import Excel


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


