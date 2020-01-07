#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/6

import logging,time
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting

#日志文件夹
if not os.path.exists(setting.LOG_DIR):
    os.mkdir(setting.LOG_DIR)

class Logger(object):
    def __init__(self,logger_name='mylogger'):
        #文件名
        self.logname = os.path.join(setting.LOG_DIR,'%s.log'%time.strftime('%Y-%m-%d %H-%M-%S'))
        self.logger = logging.getLogger(logger_name)
        #设置log等级
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] [%(filename)s|%(funcName)s] [line:%(lineno)d] %(levelname)-8s:%(message)s')

    def __console(self,level,message):
        #创建一个FileHandler，用于写到本地日志文件
        fh = logging.FileHandler(self.logname,encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        #创建一个StreamHandler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        #这两行代码是为了避免日志重复输出
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()

    #共外部调用函数
    def debug(self,message):
        self.__console('debug',message)

    def info(self,message):
        self.__console('info',message)

    def warning(self,message):
        self.__console('warning',message)

    def error(self,message):
        self.__console('error',message)

if __name__ == '__main__':
    Logger().debug("123456786")

