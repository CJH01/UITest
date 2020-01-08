#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/8
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from config import setting
from public.models import myunit,screenshot
from public.pageObj.setupPage import SetupPage
from public.pageObj.loginPage import LoginPage
from public.models.log import Logger
from public.models import driver
from time import sleep

log = Logger()
f_login = open(setting.TEST_DATA_YAML+ '/'+ 'login_data.yml',encoding='utf-8')
logindata = yaml.load(f_login,yaml.FullLoader)
f_login.close()
ph = logindata[1]['data']['phone']
pwd = logindata[1]['data']['password']

try:
    f_setup = open(setting.TEST_DATA_YAML + '/'+'mysetup_data.yml',encoding='utf-8')
    setupdata = yaml.load(f_setup,yaml.FullLoader)
except FileNotFoundError as file:
    log.error("文件不存在：{0}".format(file))

@ddt.ddt
class My_UI(myunit.MyTest):
    """首页设置"""
    def user_login(self,phone,pwd):
        """
        登录
        :param phone:
        :param pwd:
        :return:
        """
        LoginPage(self.driver).test_phone_login(phone,pwd)

    def exit_login(self):
        """
        退出登录
        :return:
        """
        self.driver.switch_to.default_content()
        SetupPage(self.driver).login_out()

    def setup_test(self,*args):
        SetupPage(self.driver).setup(*args)

    @ddt.data(*setupdata)
    def test_setup(self,datayaml):
        """
        首页-设置操作
        :param datayaml:
        :return:
        """
        log.info("当前执行测试用例ID->{0}；测试点->{1}".format(datayaml['id'],datayaml['detail']))
        #调用登录方法
        self.user_login(phone=ph,pwd=pwd)
        #调用设置接口
        self.setup_test(setupdata[0]['nick'],setupdata[0]['sign'],setupdata[0]['sex'])
        po = SetupPage(self.driver)



# if __name__ == '__main__':
#     My_UI().user_login(phone=ph,pwd=pwd)
#     My_UI().setup_test(setupdata[0]['nick'],setupdata[0]['sign'],setupdata[0]['sex'])
#     sleep(3)


