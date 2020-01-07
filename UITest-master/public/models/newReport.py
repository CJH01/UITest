#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/6

import os

#生成最新的测试报告文件
def new_report(testreport):
    #列举testreport目录下的所有文件名和文件夹，列表形式返回
    lists = os.listdir(testreport)
    #sort按key的关键字升序排列，lambda入参fn为lists列表元素，获取文件最后修改时间
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" +fn))
    #获取最新文件的绝对路径，列表中最后一个值，文件夹+文件名
    file_new = os.path.join(testreport,lists[-1])
    return file_new