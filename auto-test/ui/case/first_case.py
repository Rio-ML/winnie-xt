# -*- coding: utf-8 -*-
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
import os
import sys



class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始')

    @classmethod
    def tearDownClass(cls):
        print('结束')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://lzt.wegui.cn/#/login")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/form/div[1]/div/div/input').send_keys('dxstest')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/form/div[2]/div/div/input').send_keys('moternmotern')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/form/div[3]/div/button').click()


    def tearDown(self):
        # for method_name, error in self._outcome.errors:
        #     if error:
        #         case_name = self._testMethodName
        #         file_path = os.path.abspath(os.path.dirname(__file__)) + '/report/' + case_name + '.png'
        #         self.driver.save_screenshot(file_path)
        time.sleep(5)
        self.driver.close()

    # @unittest.skip('不执行')
    # 校验模块指示文字是否一致
    def test_01(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//div[@class='icon'][position()=3]").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'初始化配置')]").click()

        # 初始化配置
        time.sleep(2)
        text = self.driver.find_element_by_xpath("//div[@index='/systemInfo' and contains(text(),'初始化配置')]").text
        if text == '初始化配置':
            print('pass')
        else:
            print('初始化配置不匹配')

        # 系统信息配置
        self.driver.find_element_by_xpath('//*[@id="init-config"]/ul/li[1]').click()
        time.sleep(2)
        text1 = self.driver.find_element_by_xpath('//*[@id="init-config"]/div/div/div[1]/span').text
        if text1 == '系统信息配置':
            print('pass')
        else:
            print('系统信息配置不匹配')

        # 房台初始化配置
        self.driver.find_element_by_xpath('//*[@id="init-config"]/ul/li[2]').click()
        time.sleep(2)
        text2 = self.driver.find_element_by_xpath('//*[@id="init-config"]/div/div/div[1]/span').text
        text8 = self.driver.find_element_by_xpath('//*[@id="init-config"]/div/div/div[2]/form/div[1]/div/button/span').text
        text9 = self.driver.find_element_by_xpath('//*[@id="init-config"]/div/div/div[2]/form/div[2]/div/span[5]').text
        if text2 == '房台初始化配置':
            print('pass')
        else:
            print('房台初始化配置不匹配')
        if text8 == '+添加':
            print('pass')
        else:
            print('+ 添加不匹配')
        if text9 == '房台类型排序将影响房台系统的房台排序':
            print('pass')
        else:
            print('房台类型排序将影响房台系统的房台排序不匹配')

        # 点单配置
        self.driver.find_element_by_xpath('//*[@id="init-config"]/ul/li[3]').click()
        time.sleep(2)
        text3 = self.driver.find_element_by_xpath('//*[@id="init-config"]/div/div/div[1]/span').text
        if text3 == '点单、收银、出品配置':
            print('pass')
        else:
            print('点单、收银、出品配置不匹配')

        # 其他配置
        self.driver.find_element_by_xpath('//*[@id="init-config"]/ul/li[6]').click()
        time.sleep(2)
        text4 = self.driver.find_element_by_xpath('//*[@id="init-config"]/div/div/div[1]/span').text
        if text4 == '其它配置':
            print('pass')
        else:
            print('其它配置不匹配')

        # 房台配置
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[5]/ul/li[2]').click()
        time.sleep(2)
        text5 = self.driver.find_element_by_xpath('//*[@id="app"]/div/section/header/div/ul/li').text
        if text5 == '房台配置':
            print('pass')
        else:
            print('房台配置不匹配')

        # 商品配置
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[5]/ul/li[3]').click()
        time.sleep(2)
        text6 = self.driver.find_element_by_xpath('//*[@id="app"]/div/section/header/div/ul/li[1]').text
        if text6 == '商品管理':
            print('pass')
        else:
            print('商品管理不匹配')
        text7 = self.driver.find_element_by_xpath('//*[@id="app"]/div/section/header/div/ul/li[2]').text
        if text7 == '套餐管理':
            print('pass')
        else:
            print('套餐管理不匹配')


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(FirstCase('test_04_login_fail'))
    # unittest.TextTestRunner().run(suite)
