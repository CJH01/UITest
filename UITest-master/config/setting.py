#coding=utf-8
import os,sys
# #绝对路径（包含文件名）
# a = os.path.abspath(__file__)
# print(a)
# #返回脚本的路径（不包含文件名）
# b = os.path.dirname(__file__)
# print(b)
# c = os.path.dirname(os.path.abspath(__file__))
# print(c)

#得到该文件的上一个路径（相当于cd..）
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#1.当导入一个模块时：import xxx，默认情况下python解析器会搜索
#  当前目录、已安装的内置模块和第三方模块，搜索路径存放在sys模块
#  的path中
#2.sys.path返回一个列表
#3.运行时修改，脚本运行后就会失效
sys.path.append(BASE_DIR)

#配置文件
CONFIG_DIR = os.path.join(BASE_DIR,"database","config.ini")
#测试用例目录
TEST_DIR = os.path.join(BASE_DIR,"testcase")
#测试报告目录
TEST_REPORT = os.path.join(BASE_DIR,"report")
#日志目录
LOG_DIR = os.path.join(BASE_DIR,"logs")
#测试数据文件
TEST_DATA_YAML = os.path.join(BASE_DIR,"testdata")
#元素控件
TEST_Element_YAML = os.path.join(BASE_DIR,"testyaml")

