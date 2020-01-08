#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/8
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.pageObj.basePage import BasePage
from public.pageObj.loginPage import LoginPage
from time import sleep
from public.models.GetYaml import getyaml
from public.models.log import Logger
from public.models import driver

testData = getyaml(setting.TEST_Element_YAML + '/'+'mysetup.yml')
log = Logger()

#继承基础类
class SetupPage(BasePage):
    """
    首页---设置页面
    """
    url = '/'
    """
    抽离元素
    """
    #鼠标悬停控件
    user_loc = (By.XPATH,testData.get_elementinfo(0))
    #菜单设置元素
    textsetup_loc = (By.LINK_TEXT,testData.get_elementinfo(1))
    #编辑元素
    edit_loc = (By.LINK_TEXT,testData.get_elementinfo(2))
    #昵称文本框
    nick_loc = (By.XPATH,testData.get_elementinfo(3))
    #签名文本框
    sign_loc = (By.XPATH,testData.get_elementinfo(4))
    #性别女
    female_Loc = (By.ID,testData.get_elementinfo(5))
    #性别男
    male_loc = (By.ID,testData.get_elementinfo(6))
    #设置省份或直辖市
    province_lco = (By.ID,testData.get_elementinfo(7))
    #城市
    city_loc = (By.ID, testData.get_elementinfo(8))
    #保存
    save_loc = (By.LINK_TEXT, testData.get_elementinfo(9))
    #取消
    cancel_loc = (By.LINK_TEXT, testData.get_elementinfo(10))
    #省份对话框
    pro_loc = (By.XPATH, testData.get_elementinfo(11))
    #地区对话框
    ci_loc = (By.XPATH, testData.get_elementinfo(12))
    # 退出登录
    login_out_loc = (By.LINK_TEXT, testData.get_elementinfo(14))

    def login(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        LoginPage(self.driver).test_phone_login('15071196254','cjh13006182363')

    def enter_setup(self):
        """
        进入设置界面
        :return:
        """
        above = self.find_element(*self.user_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(1)
        self.find_element(*self.textsetup_loc).click()
        sleep(1)

    def enter_edit(self):
        """
        进入编辑状态
        :return:
        """
        self.find_element(*self.edit_loc).click()

    def set_nick(self,nick):
        #清空昵称文本框并录入数据
        self.find_element(*self.nick_loc).clear()
        self.find_element(*self.nick_loc).send_keys(nick)

    def set_sign(self,sign):
        #清空签名文本框并录入数据
        self.find_element(*self.sign_loc).clear()
        self.find_element(*self.sign_loc).send_keys(sign)

    # *表示接收任意多个参数，并放入元组中
    def set_province(self,province):
        """
        设置地区
        :param data:
        :return:
        """
        self.find_element(*self.pro_loc).click()
        # 先定位到下拉菜单
        ul = self.find_element(*self.province_lco)
        # 再对下拉菜单中的选项进行选择
        ul.find_element_by_xpath('li'+'[{0}]'.format(province)).click()

    def set_city(self, city):
        """
        设置城市
        :param data:
        :return:
        """
        #弹出城市下拉列表
        self.find_element(*self.ci_loc).click()
        # 先定位到下拉菜单
        ul = self.find_element(*self.city_loc)
        # 再对下拉菜单中的选项进行选择
        ul.find_element_by_xpath('li' + '[{0}]'.format(city)).click()

    def set_sex(self,sex):
        """
        设置性别
        :param sex:
        :return:
        """
        if sex == '男':
            self.find_element(*self.male_loc).click()
        else:
            self.find_element(*self.female_Loc).click()

    def save(self):
        """
        保存设置
        :return:
        """
        self.find_element(*self.save_loc).click()

    def cancel(self):
        """
        取消
        :return:
        """
        self.find_element(*self.cancel_loc).click()

    def login_out(self):
        """
        退出登录
        :return:
        """
        above = self.find_element(*self.user_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(2)
        self.find_element(*self.login_out_loc).click()

    #包含一组动作：设置
    def setup(self,nick,sign,sex):
        self.enter_setup()
        self.enter_edit()
        self.set_nick(nick)
        self.set_sign(sign)
        self.set_sex(sex)
        self.save()

if __name__ == '__main__':
    setup = SetupPage(driver.browser())
    setup.login()
    setup.enter_setup()
    sleep(3)
    driver.browser().quit()