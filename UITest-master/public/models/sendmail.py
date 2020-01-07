#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/6

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from public.models.newReport import new_report
from public.models.readConfig import ReadConfig
import win32com.client as win32
import datetime
import pythoncom

# 读取config.ini配置文件
subject = ReadConfig().get_email('subject')
address = ReadConfig().get_email('address')
app = ReadConfig().get_email('app')
cc = ReadConfig().get_email('cc')
on_off = ReadConfig().get_email('on_off')

#发送邮件
class send_email():
    def outlook(self,file_new):
        #固定写法
        outlook = win32.Dispatch("%s.Application" % app)
        #固定写法
        mail = outlook.CreateItem(0)
        #收件人
        mail.To = address
        #抄送人
        #mail.CC = cc
        #邮件主题
        mail.Subject = str(datetime.datetime.now())[0:19]+'%s' %subject

        f = open(file_new,'rb')
        mail.Body = f.read()
        f.close()
        # content = """
        # 生成报告中......
        # 报告已生成......
        # 报告已邮件发送......
        # """
        # mail.Body = content
        report = new_report(setting.TEST_REPORT)
        #mail.Attechments.Add(report)
        mail.Send()


if __name__ == '__main__':
    send_email().outlook()
    print("send email ok!")