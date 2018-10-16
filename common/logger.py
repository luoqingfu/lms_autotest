import logging

import time

import os

import readConfig

projectPath = readConfig.ProjectPath
class Logging():
    """日志类在每个class头部写入，记录日志"""
    def __init__(self, log):
        global log_path
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))   # 创建一个handler，用于写入日志文件，用于写入日志文件
        result_path = os.path.join(projectPath,"report")
        if not os.path.exists(result_path):
            os.mkdir(result_path)
        # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
        log_path = os.path.join(result_path,rq)
        if not os.path.exists(log_path):
            os.mkdir(log_path)

        self.logger = logging.getLogger(log)  # 创建一个logger
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(os.path.join(log_path+ "/output.log"), encoding="UTF-8")
        fh.setLevel(logging.INFO)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return self.logger

    def get_logPath(self):
        return log_path
