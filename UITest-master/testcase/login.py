#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/7
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from config import setting
from public.models import myunit,screenshot
from public.pageObj.loginPage import LoginPage
from public.models.log import Logger

try:
    f = open(setting.TEST_DATA_YAML + '/' +'login_data.yml',encoding='utf-8')
    testData = yaml.load(f,yaml.FullLoader)
    print(testData)
    f.close()
except FileNotFoundError as file:
    log = Logger()
    log.error("文件不存在:{0}".format(file))

@ddt.ddt
class My_UI(myunit.MyTest):
    def phone_login_verify(self,phone,password):
        """
        手机号密码登录
        :param phone:
        :param password:
        :return:
        """
        LoginPage(self.driver).test_phone_login(phone,password)

    @ddt.data(*testData)
    def test_login(self,datayaml):
        """
        真正的执行登录操作
        :param datayaml:加载login_data登录测试数据
        :return:
        """
        log = Logger()
        log.info("当前执行测试用例ID->{0};测试点->{1}".format(datayaml['id'],datayaml['detail']))
        #调用登录方法
        self.phone_login_verify(datayaml['data']['phone'],datayaml['data']['password'])
        po = LoginPage(self.driver)
        if datayaml['screenshot'] == 'phone_and_pwd_success':
            #断言
            self.assertFalse(po.login_success(self.driver))
            log.info("登录成功")
            screenshot.insert_img(self.driver, datayaml['screenshot'] + '.png')
        else:
            log.info("检查点->{0}".format(po.login_fail_hint()))
            #断言
            self.assertEqual(po.login_fail_hint(),datayaml['check'][0],"登录异常，返回实际结果是->:{0}".format(po.login_fail_hint()))
            #log.info("登录异常，返回实际结果是->:{0}".format(po.login_fail_hint()))
            screenshot.insert_img(self.driver,datayaml['screenshot']+'.png')

if __name__ == '__main__':
    unittest.main()