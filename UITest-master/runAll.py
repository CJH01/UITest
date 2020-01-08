#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/7
import os,sys
sys.path.append(os.path.dirname(__file__))
from config import setting
import unittest,time
from package.HTMLTestRunner import HTMLTestRunner
from public.models.newReport import new_report
from public.models.sendmail import send_email
from public.models.readConfig import ReadConfig

#邮件开关配置
on_off = ReadConfig().get_email('on_off')

if not os.path.exists(setting.TEST_REPORT):
    os.makedirs(setting.TEST_REPORT + '/'+ "screenshot")

def add_case(test_path=setting.TEST_DIR):
    """
    加载所有的测试用例
    :param test_path:
    :return:
    """
    discover = unittest.defaultTestLoader.discover(test_path,pattern='*.py')
    return discover

def run_case(all_case,result_path=setting.TEST_REPORT):
    """
    执行所有用例
    :param all_case:
    :param result_path:
    :return:
    """
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = result_path+ '/'+now+' result.html'
    if all_case is not None:
        print('if-suit')
        with open(filename,'wb') as fp:
            runner = HTMLTestRunner(fp,title='抽屉UI自动化测试报告',description='Test Description')
            runner.run(all_case)
            fp.close()
            """
            发送邮件
            """
            if on_off == 'on':
                send_email().outlook() #发送邮件

            else:
                print("邮件发送开关配置关闭，请打开后自动发送测试报告")
    else:
        print("没有测试用例")

if __name__ == '__main__':
    case = add_case()
    print(case)
    run_case(case)

