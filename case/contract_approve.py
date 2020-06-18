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
        # mobile_emulation = {'deviceName': 'iPhone X'}
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('mobileEmulation', mobile_emulation)
        # # Windows 配置 开始
        # self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        # # Windows 配置 结束
        # # mac 配置 开始
        # # options.binary_location = "/Applications/IT/Google Chrome.app/Contents/MacOS/Google Chrome"
        # # chrome_driver_binary = "/usr/local/bin/chromedriver"
        # # self.driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        # # mac 配置 结束
        self.driver = DriverInit().driver
        # self.driver_init.open_url("http://wxadmin.wegui.cn/admin/#/")
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
