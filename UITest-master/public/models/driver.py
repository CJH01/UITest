#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/6
from selenium import webdriver
def browser():
    """
    启动浏览器驱动
    :return: 返回浏览器驱动URL
    """
    try:
            # host = '127.0.0.1:4444'
            #
            # driver = Remote(command_executor='http://'+host+'/wd/hub',
            #                 desired_capabilities={
            #                     'platfrom':'ANY',
            #                     'browserName':'chrome',
            #                     'version':"",
            #                     'javascriptEnabled':True
            #                 })
        driver = webdriver.Firefox()
        return driver
    except Exception as msg:
        #{0}占位符
        print("驱动异常->{0}".format(msg))

if __name__ == '__main__':
    print(browser())