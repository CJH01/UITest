#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/6

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
import configparser

#配置文件路径
config_path = setting.CONFIG_DIR
#读取配置文件的方法
config = configparser.ConfigParser()
print(config_path)
config.read(config_path,'utf-8')

#封装读取配置文件的方法
class ReadConfig():
    #读取邮箱配置
    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value

    #读取数据库配置
    def get_mysql(self,name):
        value = config.get('DATABASE',name)
        return value

    #读取url
    def get_url(self,name):
        value = config.get('WebURL',name)
        return value

if __name__ == '__main__':
    print(ReadConfig().get_email('cc'))
    print(ReadConfig().get_url('url'))