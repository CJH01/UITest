#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/6
from selenium.webdriver.common.by import By
from time import sleep
from public.pageObj.basePage import BasePage
from public.models import driver
from public.models.GetYaml import getyaml
from config import setting
import selenium
from selenium.webdriver.common.action_chains import ActionChains

testData = getyaml(setting.TEST_Element_YAML + '/' +'login.yml')

class LoginPage(BasePage):
    """
    用户登录界面
    """
    url = '/'
    dig_login_button_loc = (By.ID,testData.get_elementinfo(0))
    def dig_login(self):
        """
        首页登录
        :return:
        """
        self.find_element(*self.dig_login_button_loc).click()
        sleep(1)

    """
    抽离元素
    """
    #手机号码输入框
    login_phone_loc = (By.XPATH,testData.get_elementinfo(1))
    #抽离元素  用户名
    username_loc = (By.XPATH,testData.get_elementinfo(3))
    #登录密码
    password_loc = (By.XPATH,testData.get_elementinfo(2))
    #登录按钮
    btn_login_loc = (By.XPATH,testData.get_elementinfo(4))
    #用户名登录
    swip_user_login_loc = (By.LINK_TEXT,testData.get_elementinfo(5))
    #忘记密码
    forget_pwd_loc = (By.LINK_TEXT,testData.get_elementinfo(6))
    #登陆失败
    login_fail_hint_loc =(By.XPATH,testData.get_CheckElementinfo(0))

    def type_username(self,username):
        """
        #输入用户名
        :param username:
        :return:
        """
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def login_phone(self,phone):
        """
        输入手机号
        :param phone:
        :return:
        """
        self.find_element(*self.login_phone_loc).send_keys(phone)

    def login_password(self,pwd):
        """
        输入密码
        :param pwd:
        :return:
        """
        self.find_element(*self.password_loc).send_keys(pwd)

    def btn_login(self):
        """
        点击登录按钮
        :return:
        """
        self.find_element(*self.btn_login_loc).click()

    def swip_user_login(self):
        """
        切换到用户名密码登录界面
        :return:
        """
        self.find_element(*self.swip_user_login_loc).click()

    def forget_pwd(self):
        """
        忘记密码，跳转到忘记密码界面
        :return:
        """
        self.find_element(*self.forget_pwd_loc).click()

    def login_fail_hint(self):
        """
        登陆失败的提示
        :return:
        """
        return self.find_element(*self.login_fail_hint_loc).text

    def login_success(self,driver):
        """
        判断登录按钮是否存在
        :return:
        """
        try:
            self.find_element(*self.dig_login_button_loc)
            return True
        except Exception as e:
            return False


# #包含一组动作：用户名登录
# def test_user_login(driver,username,password):
#     login_page = loginBox(driver)
#     #切换到用户名密码登录
#     login_page.swip_user_login()
#     login_page.type_username(username)
#     login_page.login_password(password)
#     login_page.btn_login()
#
    #包含一组动作：手机号登录
    def test_phone_login(self,phone,password):
        self.open()
        self.dig_login()
        self.login_phone(phone)
        self.login_password(password)
        sleep(1)
        self.btn_login()
        sleep(2)
#
# def forget_pwd(driver):
#     login_page = loginBox(driver)
#     login_page.forget_pwd()
#
# #弹出登录框
# def loginBox(driver):
#     login_page = LoginPage(driver)
#     login_page.open()
#     login_page.dig_login()
#     sleep(1)
#     return login_page
#
# if __name__ == '__main__':
#     driver = driver.browser()
#     username = 'cjh001'
#     phone=13566652213
#     password = 4546745412344
#     test_user_login(driver,username,password)
#     #test_phone_login(driver,phone,password)
#     sleep(3)
#     driver.quit()


