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

    @unittest.skip('不执行')
    # 微信管理端 提交一个审批
    def test_001(self):
        self.driver.implicitly_wait(30)
        self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
        self.rp.wx_login('xiaod90', '123456')
        self.rb.contract_base()
        self.driver.close()
        # self.driver.back()

    # 后台管理 增加VIP优惠券
    def test_002(self):
        self.driver.implicitly_wait(30)
        self.rp.open_url("http://admin.wegui.cn/#/")
        self.driver.maximize_window()
        self.rp.web_login('xiaodwx', '123456')
        self.rp.open_web_menu('运营管理')
        self.rp.open_web_menu('优惠券管理')
        self.rp.web_button("添加优惠券")
        self.rp.web_input_text("优惠券名称", "测试VIP01")
        self.rp.web_button("优惠券类型")
        self.rp.web_button("vip券")
        self.rp.web_button("抵扣类型")
        self.rp.web_button("vip券-抵扣现金")
        self.rp.web_input_text("vip等级", "ssr")
        self.rp.web_input_text("简介", "UI自动化")
        self.rp.web_button("所属商户")
        self.rp.web_button("商户", "测试合同226")
        self.rp.web_button("添加优惠券-确定")


if __name__ == '__main__':
    unittest.main()
