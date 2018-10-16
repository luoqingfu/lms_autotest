# -*- coding: utf-8 -*-
import random
import time
from datetime import datetime
import xlrd
from xlrd import xldate_as_tuple
from xlutils.copy import copy


from testFile import DATAPATH
from common.logger import Logging

logger_random = Logging("Random").getlog()
logger_excel = Logging("Excel").getlog()
class Excel():
    def __init__(self, filename):
        """filename = excel文件名称，row = 从excel表的第几行开始读取"""
        logger_excel.info("加载{}excel表".format(filename))
        self.filename = filename

        self.workbook = xlrd.open_workbook(DATAPATH+
            r"/{}.xls".format(
                filename))  #加载EXCLE文件

        self.table = self.workbook.sheets()[0]  #获取文件sheet

        self.nrows = self.table.nrows   #excel表格中的行数

        self.ncols = self.table.ncols #excel表格中的列数

    def read_excel(self, row):
        """读取excel表格内的文件并且使用字典表进行储存"""
        list = []
        for r in range(row, self.nrows):
            app = {}
            for col in range(self.ncols):
                value = self.table.cell(r, col).value
                ctype = self.table.cell(r, col).ctype
                if ctype == 0:
                    value = ""
                elif ctype == 1:
                    value = value
                elif ctype == 2:
                    value = int(value)
                elif ctype == 3:
                    date = datetime(*xldate_as_tuple(value, 0))
                    value = date.strftime("%Y/%m/%d  %H:%M:%S")
                elif ctype == 4:
                    if value == 0:
                        value = False
                    if value == 1:
                        value = True
                elif ctype == 5:
                    value = "错误~~~~~"
                app[self.table.cell(row-1, col).value] = value
            list.append(app)
        logger_excel.info("读取EXCEL表中的数据：{}".format(list))
        return list
    def write_excel(self,datas,row = 1):
        """写如excel表格"""
        new_excel = copy(self.workbook)
        ws = new_excel.get_sheet(0)
        if len(datas) == 0:
            print("错误！！！！")
        else:
            for col in range(self.ncols):
                print(datas[col], "datas[col]")
                if datas[col] != "" or datas[col] == None:
                    ws.write(row, col, datas[col])
            new_excel.save(DATAPATH+
                r"\{}.xls".format(
                    self.filename))
    def write_excel_rol(self,col,row, data):
        new_excel = copy(self.workbook)
        ws = new_excel.get_sheet(0)
        print('写入中')
        ws.write(col, row, data)
        new_excel.save(DATAPATH +
                       r"/{}.xls".format(
                           self.filename))

"""随机字符的处理"""

class Random():
    """给出随机数的范围"""
    def get_random_number(self,list):
        logger_random.info("输入随机的范围：%s" %list)
        return int(random.uniform(*list))
    """给出集合，从中随机抽取一个"""
    def get_random_list(self,list):
        return random.choice(list)
    """随机选取字母。0：代表大小写字母。-1：代表小写字母。1：代表大写字母"""
    def get_random_letter(self,letter_size = 0):
        list_lowercase = []
        list_majuscule = []
        #小写字母集合
        for i in range(65, 91):
            list_lowercase.append(chr(i))
        #大写字母集合
        for i in range(97, 123):
            list_majuscule.append(chr(i))
        #大小写全部字母
        letter = list_lowercase+list_majuscule
        if letter_size == 0:
            return self.get_random_list(letter)
        elif letter_size == -1:
            return self.get_random_list(list_lowercase)
        elif letter_size == -2:
            return self.get_random_list(list_majuscule)
    """随机选取键盘常用符号"""
    def get_random_symbol(self, symboltype = 0):
        english_list = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(",")","_"
            , "+", "`", "-", "=", "{", "}", "|", ":", " ", "<", ">", "?",
                "[", "]", ";", "'", ",", ".", "/"]
        china_list = ["~", "！", "@", "#", "￥", "%", "……", "&", "*", "（", "）", "——"
            , "+", "·", "-", "=", "【", "】", "、", "{", "} ", "|", "：", "“",
                "；", "‘", "《", "》", "？", "，", "。", "、", " "]
        symbol = english_list+china_list
        if symboltype == 0:
            return self.get_random_list(symbol)
        elif symboltype == -1:
            return self.get_random_list(english_list)
        elif symboltype == -2:
            return self.get_random_list(china_list)
"""字符串的处理"""
class String():
    # 截取URL路径
    def url_split(self, url, symbol="?"):
        return url.split(symbol)[0]

    # 字符串转换为浮点型
    def get_float(self, str):
        return float(str)
class Time():
    # 当前时间转换器
    def get_time(self, symbol="-", years=False):
        if years:
            time_stamp = time.localtime(time.time() + 31536000)
        else:
            time_stamp = time.localtime(time.time())
        return time.strftime("%Y{}%m{}%d".format(symbol, symbol), time_stamp)















