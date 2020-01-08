#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/6
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException,NoSuchWindowException,NoAlertPresentException,NoSuchElementException
from public.models.log import Logger
from public.models.readConfig import ReadConfig

#读取配置文件
login_url = ReadConfig().get_url('url')
log = Logger()

#PageObject模式设计思想：把元素和方法按照页面抽象出来，分离成一定的对象
class BasePage(object):
    """
    用于页面对象类的继承
    """
    #初始化参数
    def __init__(self,driver,url=login_url,parent=None):
        self.base_url = url
        self.driver = driver
        self.parent = parent
        self.timeout = 10

    #地址断言
    def on_page(self):
        """
        URL地址断言
        :return:
        """
        return self.driver.current_url == (self.base_url+self.url)

    #打开登录页面
    def _open(self):
        url = self.base_url
        self.driver.get(url)

    #定义open方法
    def open(self):
        self._open()

    #找多个元素
    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            log.error("{0}页面中未能找到{1}元素".format(self,loc))

    def find_element(self, *loc):
        """
        定位单个元素
        :param loc:
        :return:
        """
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            log.error("{0}页面中未能找到{1}元素".format(self,loc))

    def switch_frame(self,loc):
        """
        多表单嵌套切换
        :param loc:
        :return:
        """
        try:
            return self.driver.switch_to_frame(loc)
        except NoSuchFrameException as msg:
            log.error("查找iframe异常->{0}".format(msg))

    def find_select(self,*loc):
        return self.driver.find_element_by_css_selector(*loc)


