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
    def setUp(self) :
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
