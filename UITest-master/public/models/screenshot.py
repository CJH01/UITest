#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/6
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting

#截图
def insert_img(driver,file_name):
    #如果screenshot文件夹不存在
    if not os.path.exists(setting.TEST_REPORT + '/'+ "screenshot"):
        os.mkdir(setting.TEST_REPORT + '/' + "screenshot")
    file_path = setting.TEST_REPORT + "/screenshot/" + file_name
    return driver.get_screenshot_as_file(file_path)