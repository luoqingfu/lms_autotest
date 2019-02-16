import smtplib
import unittest

import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime as dt


import readConfig
from common import logger
from common.HTMLTestRunner import HTMLTestRunner

log = logger.Logging("run").getlog()
def get_case_list():
    """获取case_list.txt文件中要执行的用例文件的名称"""
    list = open(os.path.join(readConfig.ProjectPath, "case_list.txt"))
    cases = []
    for value in list.readlines():
        data = str(value)
        if data != "" and not data.startswith("#"):
            cases.append(data.replace("\n", ""))
    #print(cases, "cases")
    return cases
def send_mail():
    # 读取测试报告内容
    with open(report_file, 'r', encoding='UTF-8') as f:
        content = f.read()

    msg = MIMEMultipart('mixed')
    # 添加邮件内容
    #msg_html = MIMEText(content, 'html', 'utf-8')
    # msg.attach(msg_html)
    content_msg = config.getConfig('mail_content')
    print(content_msg)
    msg_content = MIMEText(content_msg.format(dt.now().strftime('%Y%m%d'), 'plain', 'utf-8'))
    msg.attach(msg_content)

    # 添加附件
    msg_attachment = MIMEText(content, 'html', 'utf-8')
    msg_attachment["Content-Disposition"] = 'attachment; filename="{0}"'.format(report_file)
    msg.attach(msg_attachment)

    msg['Subject'] = mail_subjet
    msg['From'] = mail_user
    msg['To'] = ';'.join(mail_to)
    try:
        # 连接邮件服务器
        s = smtplib.SMTP_SSL(mail_host, 465)
        # 登陆
        s.login(mail_user, mail_pwd)
        # 发送邮件
        s.sendmail(mail_user, mail_to, msg.as_string())
        # 退出
        s.quit()
    except Exception as e:
        print("Exceptioin ", e)


def get_list():
    """获取case_list.txt文件中要执行的用例文件，返回以文件为单位的list集合"""
    suite_module = []
    list = get_case_list()
    for value in list:
        case_path = os.path.join(logger.projectPath, "testCase")
        discover = unittest.defaultTestLoader.discover(case_path,   pattern=value.split("/")[-1]+'.py', top_level_dir=None)
        suite_module.append(discover)
    #print(suite_module, "suite_module")
    return suite_module

if __name__ == '__main__':
    result_html = logger.Logging("Run").get_logPath()
    config = readConfig.ReadConfig()
    title = config.getConfig("title") + "测试报告"
    browser = config.getConfig("browser")
    description = "浏览器：" + browser
    testunit = unittest.TestSuite()
    list = get_list()
    if len(list) > 0:
        for suite in get_list():
            testunit.addTest(suite)
    filename = os.path.join(result_html, "result.html")
    print(filename)
    fp = open(filename, "wb")
    renner = HTMLTestRunner(stream=fp, title=title, description=description)
    renner.run(testunit)
    fp.close()
    # 邮件服务器
    mail_host = config.getConfig('mail_host')
    # 发件人地址
    mail_user = config.getConfig('mail_user')
    # 发件人密码
    mail_pwd = config.getConfig('mail_pwd')
    # 邮件标题
    mail_subjet = config.getConfig('mail_subjet').format(dt.now().strftime('%Y%m%d'))
    # 收件人地址list
    mail_tolist= config.getConfig('mail_to').split(',')
    mail_to = []
    for n in range(len(mail_tolist)):
        mail_to.append(mail_tolist[n])
    report_file = filename
    # 发送测试报告邮件

    send_mail()
    print('Send Test Report Mail Now...')

