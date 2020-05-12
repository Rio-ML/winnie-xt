# -*- coding:utf-8 -*-
# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
from case import common_operation

'''
PersonManage人事管理

'''


class PersonManage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://lzt.wegui.cn/#/login")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@placeholder='登陆账号']").send_keys('dxstest')
        self.driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys('dxs123123')
        self.driver.find_element_by_xpath("//button[@type='button']").click()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

    # @unittest.skip('不执行')
    # 添加员工
    def test_001(self):
        self.driver.implicitly_wait(30)
        common_operation.IntoModule.into_personnel(self, 'staff')
        self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'添加员工')]").click()


if __name__ == '__main__':
    unittest.main()
