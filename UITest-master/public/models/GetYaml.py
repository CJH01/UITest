#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/6
import yaml

class getyaml:
    def __init__(self,filepath):
        self.path = filepath

    def get_yaml(self):
        """
        加载yaml数据文件
        :param path:文件路径
        :return: 返回数据
        """
        try:
            f = open(self.path,encoding='utf-8')
            data = yaml.load(f,Loader=yaml.FullLoader)
            f.close()
            return data
        except Exception as msg:
            print("异常消息->{0}".format(msg))

    def alldata(self):
        data = self.get_yaml()
        return data

    #testcase字典长度
    def caselen(self):
        data = self.alldata()
        length = len(data['testcase'])
        return length

    # check字典长度
    def checklen(self):
        data = self.alldata()
        length = len(data['check'])
        return length

    #elementinfo
    def get_elementinfo(self,i):
        """
            获取testcase项的element_info元素
             :param i: 位置序列号
             :return: 返回element_info元素数据
            """
        data = self.alldata()
        return data['testcase'][i]['element_info']

    #find_type
    def get_find_type(self,i):
        data = self.alldata()
        return data['testcase'][i]['find_type']

    # operate_type
    def get_operate_type(self, i):
        data = self.alldata()
        return data['testcase'][i]['operate_type']

    #check_element_info
    def get_CheckElementinfo(self,i):
        data = self.alldata()
        return data['check'][i]['element_info']

    #find_type
    def get_CheckFindType(self,i):
        data = self.alldata()
        return data['check'][i]['find_type']

    #operate_type
    def get_CheckOperate_type(self,i):
        data = self.alldata()
        return data['check'][i]['operate_type']


if __name__ == '__main__':
    path = 'D:/PythonProject/pythonSelenium/UIMaster/testyaml/mysetup.yml'
    print(getyaml(path).alldata())
