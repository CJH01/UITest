#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jiaho
# datetime:2020/1/6

from .driver import browser
import unittest

class MyTest(unittest.TestCase):
    """
    自定义MyTest类
    """

    def setUpClass(cls) :
        cls.driver = browser()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def tearDownClass(cls):
        cls.driver.quit()
