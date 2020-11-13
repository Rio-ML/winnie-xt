# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
import time
from ui.business.register_business import RegisterBusiness
from ui.page.element_page import RegisterPage
from ui.util.DriverInit import DriverInit
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from ui.page.element_page import SessionToken
import requests
import json

'''
管理后台权限-合作商，商户，出资人
'''

class TestWebPower(unittest.TestCase):

    def setUp(self):
        self.driver = DriverInit().driver
        self.rb = RegisterBusiness(self.driver)
        self.rp = RegisterPage(self.driver)
        self.st = SessionToken()

    def tearDown(self):
        time.sleep(3)
        # self.driver.close()

    @unittest.skip('不执行')
    # 微信管理端 提交一个审批
    def test_001(self):
        self.driver.implicitly_wait(30)
        self.rp.open_url("http://admin.wegui.cn/")
        self.rp.web_login('xiaod', 'abc123')
        self.rb.contract_base()
        self.driver.close()
        # self.driver.back()

    # 平台xiaod、合作商xd05、商户xd200、出资人xd153（web没有此权限）-提现管理，去掉“待验证”的筛选条件
    def test_002(self):
        self.driver.implicitly_wait(30)
        self.rp.open_url("http://admin.wegui.cn/")
        self.driver.maximize_window()
        self.rp.web_login('xd200', 'abc123')
        self.rp.open_web_menu('财务管理')
        self.rp.open_web_menu('提现管理')
        # 提现管理类型
        type_text = self.driver.find_elements_by_xpath("(//div[@class='withdrawType'])[2]/child::*")
        print(type_text.text)
        # lists = []
        # for i in type_text:
        #     a = i.text
        #     lists.append(a)
        # print(lists)
        # if "待验证" not in lists:
        #     print("pass")
        # else:
        #     print("fail")


