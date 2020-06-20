# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from business.register_business import RegisterBusiness
from page.element_page import RegisterPage
from util.DriverInit import DriverInit

'''
微信管理端审批
'''


class TestReserveTable(unittest.TestCase):

    def setUp(self):
        self.driver = DriverInit().driver
        self.rb = RegisterBusiness(self.driver)
        self.rp = RegisterPage(self.driver)

    def tearDown(self):
        time.sleep(5)
        # self.driver.close()

    # @unittest.skip('不执行')
    # 提交一个审批
    def test_001(self):
        self.driver.implicitly_wait(30)
        # self.driver.maximize_window()
        self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
        self.rp.login('xiaod90', '123456')
        self.rb.contract_base()
        self.driver.close()
        # self.driver.back()


if __name__ == '__main__':
    unittest.main()
