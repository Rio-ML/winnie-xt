# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from business.register_business import RegisterBusiness
from page.element_page import RegisterPage
from util.DriverInit import DriverInit
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import requests
import json

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
        self.driver.close()

    # @unittest.skip('不执行')
    # 微信管理端 提交一个审批
    def test_001(self):
        self.driver.implicitly_wait(30)
        self.rp.open_url("http://192.168.10.121:8080")
        self.rp.wx_login('lan1', '123456')
        self.rb.contract_base()
        self.driver.close()
        # self.driver.back()

    def test_002(self):
        self.driver.implicitly_wait(30)
        self.rp.open_url("http://192.168.10.121:8080")
        self.rp.wx_login('lan1', '123456')
        self.rp.open_xt_menu('发货申请(新)')
        self.driver.close()
        # self.driver.back()

    @unittest.skip('不执行')
    # 后台管理 增加VIP优惠券
    def test_003(self):
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

    @unittest.skip('不执行')
    # 快递柜 标签是否含有所属合作商
    def test_004(self):
        self.driver.implicitly_wait(30)
        self.rp.open_url("http://kdg.wegui.cn/#/")
        # self.driver.maximize_window()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='登陆账号']"))).send_keys("admin")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='请输入密码']"))).send_keys("Admin!1234")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='button']"))).click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@title='区域管理']"))).click()
        names = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//th[@colspan='1']/div")))
        lists = []
        for i in names:
            a = i.text
            lists.append(a)
            print(a, i.get_attribute("div"))  # 打印遍历标签出来的内容和获取div属性的内容
        print(lists)
        print(lists[0].split('\n'))
        print(len(lists[0].split('\n')))

    # @unittest.skip('不执行')
    # 商户权限
    # 【管理员】快捷管理（配置），机柜管理，订单管理，收益记录，数据统计（配置），兑换统计（写死xd1），提现（配置），设置
    # 【运维员】快捷管理（配置），机柜管理，订单管理，设置
    # 【财务员】快捷管理（配置），收益记录，数据统计，提现（配置），设置
    # 【总营收管理员】快捷管理（配置），机柜管理，收益记录，设置
    # 【分成管理员】快捷管理（配置），机柜管理，收益记录，提现（配置），设置
    def test_005(self):
        url = 'http://debug2.wegui.cn/v1/users/hYerDH4nHm'
        headers = {"Content-Type": "application/json",
                   "Xi-App-Id": "0a8020002101b2ddc7626fca179adf70",
                   "Xi-Session-Token": "r:8ceacf261f6da1b17ecbbb2b86db29d0"}
        role_list = ['main', 'operator', 'accountant', 'partner', 'regulator']
        for role in role_list:
            data = self.rp.wx_power(role, True, True, True, True, True, True)
            print(data)
            put_request = requests.put(url, data=data, headers=headers)
            print(put_request)
            self.driver.implicitly_wait(30)
            self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
            self.rp.wx_login('shop', 'abc123')
            names = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='router_desc']")))
            right_list_base = self.rp.wx_power_list(role)
            right_list = right_list_base.copy()
            lists = []
            for i in names:
                a = i.text
                lists.append(a)
            if right_list == lists:
                print(role + "权限正确", '\n', right_list)
            else:
                print(role + "权限错误", '\n', right_list, '\n', lists)
            # self.rp.wx_logout()

    # @unittest.skip('不执行')
    # 商户权限-无快捷管理权限
    def test_006(self):
        url = 'http://debug2.wegui.cn/v1/users/hYerDH4nHm'
        headers = {"Content-Type": "application/json",
                   "Xi-App-Id": "0a8020002101b2ddc7626fca179adf70",
                   "Xi-Session-Token": "r:8ceacf261f6da1b17ecbbb2b86db29d0"}
        role_list = ['main', 'operator', 'accountant', 'partner', 'regulator']
        for role in role_list:
            data = self.rp.wx_power(role, True, True, True, False, True, True)
            requests.put(url, data=data, headers=headers)
            self.driver.implicitly_wait(30)
            self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
            self.rp.wx_login('shop', 'abc123')
            names = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='router_desc']")))
            right_list_base = self.rp.wx_power_list(role)
            right_list = right_list_base.copy()
            right_list.remove('快捷管理')
            lists = []
            for i in names:
                a = i.text
                lists.append(a)
            if right_list == lists:
                print(role + "权限正确")
            else:
                print(role + "权限错误", '\n', right_list, '\n', lists)
            self.rp.wx_logout()

    @unittest.skip('不执行')
    # 合作商权限
    # 【管理员】
    # 【运维员】
    # 【财务员】
    # 【总营收管理员】
    # 【分成管理员】
    def test_007(self):
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

    @unittest.skip('不执行')
    # 出资人权限
    # 【管理员】
    # 【运维员】
    # 【财务员】
    # 【总营收管理员】
    # 【分成管理员】
    def test_008(self):
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

    @unittest.skip('不执行')
    # 区域经理权限
    # 【管理员】
    # 【运维员】
    # 【财务员】
    # 【总营收管理员】
    # 【分成管理员】
    def test_009(self):
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