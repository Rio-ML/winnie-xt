# -*- coding: utf-8 -*-
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
        time.sleep(3)
        self.driver.close()

    @unittest.skip('不执行')
    # 微信管理端 提交一个审批
    def test_001(self):
        self.driver.implicitly_wait(30)
        self.rp.open_url("http://192.168.10.121:8080")
        self.rp.wx_login('lan1', '123456')
        self.rb.contract_base()
        self.driver.close()
        # self.driver.back()

    @unittest.skip('不执行')
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
    # 【main管理员】快捷管理（配置），机柜管理，订单管理，收益记录，数据统计（配置），兑换统计（写死xd1），提现（配置），设置
    # 【operator运维员】快捷管理（配置），机柜管理，订单管理，设置
    # 【accountant财务员】快捷管理（配置），收益记录，数据统计（配置），提现（配置），设置
    # 【partner总营收管理员】快捷管理（配置），机柜管理，收益记录，设置
    # 【regulator分成管理员】快捷管理（配置），机柜管理，收益记录，提现（配置），设置
    def test_005(self):
        url = 'http://debug2.wegui.cn/v1/users/hYerDH4nHm'
        role_list = ['main', 'operator', 'accountant', 'partner', 'regulator']
        for role in role_list:
            data = self.rp.wx_shop_power(role, True, True, True, True, True, True)
            requests.put(url, data=data, headers=self.rp.web_headers())
            self.driver.implicitly_wait(30)
            self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
            self.rp.wx_login('shop', 'abc123')
            names = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='router_desc']")))
            right_list_base = self.rp.wx_shop_power_list(role)
            right_list = right_list_base.copy()
            lists = []
            for i in names:
                a = i.text
                lists.append(a)
            if right_list == lists:
                print('所有权限:', role + "权限正确", right_list)
            else:
                print('所有权限:', role + "权限错误", '\n', right_list, '\n', lists)
            self.rp.wx_logout()

    @unittest.skip('不执行')
    # 商户权限-无提现模块
    def test_006(self):
        url = 'http://debug2.wegui.cn/v1/users/hYerDH4nHm'
        role_list = ['main', 'operator', 'accountant', 'partner', 'regulator']
        for role in role_list:
            data = self.rp.wx_shop_power(role, True, True, False, True, True, True)
            requests.put(url, data=data, headers=self.rp.web_headers())
            self.driver.implicitly_wait(30)
            self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
            self.rp.wx_login('shop', 'abc123')
            names = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='router_desc']")))
            right_list_base = self.rp.wx_shop_power_list(role)
            right_list = right_list_base.copy()
            if '提现' in right_list:
                right_list.remove('提现')
                lists = []
                for i in names:
                    a = i.text
                    lists.append(a)
                if right_list == lists:
                    print('关闭提现权限:', role + "权限正确", right_list)
                else:
                    print('关闭提现权限:', role + "权限错误", '\n', right_list, '\n', lists)
                # self.rp.wx_logout()

    @unittest.skip('不执行')
    # 商户权限-无快捷管理权限
    def test_007(self):
        url = 'http://debug2.wegui.cn/v1/users/hYerDH4nHm'
        role_list = ['main', 'operator', 'accountant', 'partner', 'regulator']
        for role in role_list:
            data = self.rp.wx_shop_power(role, True, True, True, False, True, True)
            requests.put(url, data=data, headers=self.rp.web_headers())
            self.driver.implicitly_wait(30)
            self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
            self.rp.wx_login('shop', 'abc123')
            names = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='router_desc']")))
            right_list_base = self.rp.wx_shop_power_list(role)
            right_list = right_list_base.copy()
            right_list.remove('快捷管理')
            lists = []
            for i in names:
                a = i.text
                lists.append(a)
            if right_list == lists:
                print('关闭快捷管理权限:', role + "权限正确", right_list)
            else:
                print('关闭快捷管理权限:', role + "权限错误", '\n', right_list, '\n', lists)
            # self.rp.wx_logout()

    @unittest.skip('不执行')
    # 商户权限-无商户基础报告权限，数据统计
    def test_008(self):
        url = 'http://debug2.wegui.cn/v1/users/hYerDH4nHm'
        role_list = ['main', 'operator', 'accountant', 'partner', 'regulator']
        for role in role_list:
            data = self.rp.wx_shop_power(role, True, True, True, True, True, False)
            requests.put(url, data=data, headers=self.rp.web_headers())
            self.driver.implicitly_wait(30)
            self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
            self.rp.wx_login('shop', 'abc123')
            names = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='router_desc']")))
            right_list_base = self.rp.wx_shop_power_list(role)
            right_list = right_list_base.copy()
            if '数据统计' in right_list:
                right_list.remove('数据统计')
                lists = []
                for i in names:
                    a = i.text
                    lists.append(a)
                if right_list == lists:
                    print('关闭数据统计权限:', role + "权限正确", right_list)
                else:
                    print('关闭数据统计权限:', role + "权限错误", '\n', right_list, '\n', lists)
                # self.rp.wx_logout()

    @unittest.skip('不执行')
    # 合作商权限
    # 【管理员】网点管理，机柜管理，订单管理，审批，合同审批，发货申请，合同审批（新），发货申请（新），收益记录，数据统计，提现（配置），满柜监控，客户报备，峰值统计，设置
    # 【运维员】网点管理，机柜管理，订单管理，审批，合同审批，发货申请，合同审批（新），发货申请（新），满柜监控，设置
    # 【财务员】审批，收益记录，数据统计，提现（配置），设置
    # 【总营收管理员】机柜管理，审批，收益记录，设置
    # 【分成管理员】机柜管理，审批，收益记录，提现（配置），设置
    def test_009(self):
        url = 'http://debug2.wegui.cn/v1/users/TnSFqkLR9D'
        role_list = ['main', 'operator', 'accountant', 'partner', 'regulator']
        for role in role_list:
            # 布尔值 web（后台登陆）,wxadmin（微信管理端），withdraw（提现）
            data = self.rp.wx_agent_power(role, True, True, True)
            requests.put(url, data=data, headers=self.rp.web_headers())
            self.driver.implicitly_wait(30)
            self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
            self.rp.wx_login('xd05', 'abc123')
            names = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='router_desc']")))
            right_list_base = self.rp.wx_agent_power_list(role)
            right_list = right_list_base.copy()
            lists = []
            for i in names:
                a = i.text
                lists.append(a)
            if right_list == lists:
                print('所有权限:', role + "权限正确", right_list)
            else:
                print('所有权限:', role + "权限错误", '\n', right_list, '\n', lists)
            # self.rp.wx_logout()

    @unittest.skip('不执行')
    # 合作商权限-无提现权限
    def test_010(self):
        url = 'http://debug2.wegui.cn/v1/users/TnSFqkLR9D'
        role_list = ['main', 'operator', 'accountant', 'partner', 'regulator']
        for role in role_list:
            # 布尔值 web（后台登陆）,wxadmin（微信管理端），withdraw（提现）
            data = self.rp.wx_agent_power(role, True, True, False)
            requests.put(url, data=data, headers=self.rp.web_headers())
            self.driver.implicitly_wait(30)
            self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
            self.rp.wx_login('xd05', 'abc123')
            names = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='router_desc']")))
            right_list_base = self.rp.wx_agent_power_list(role)
            right_list = right_list_base.copy()
            if '提现' in right_list:
                right_list.remove('提现')
                lists = []
                for i in names:
                    a = i.text
                    lists.append(a)
                if right_list == lists:
                    print('关闭数据统计权限:', role + "权限正确", right_list)
                else:
                    print('关闭数据统计权限:', role + "权限错误", '\n', right_list, '\n', lists)
                self.rp.wx_logout()

    # @unittest.skip('不执行')
    # 出资人权限-无提现权限
    # 【管理员】机柜管理，订单管理，收益统计，提现，数据概况，数据分析，设置
    def test_011(self):
        url = 'http://debug2.wegui.cn/v1/users/MCenqjtx4R'
        role_list = ['main']
        for role in role_list:
            # 布尔值 web（后台登陆）,wxadmin（微信管理端），withdraw（提现）
            data = self.rp.wx_investor_power(role, True, True, True)
            requests.put(url, data=data, headers=self.rp.web_headers())
            self.driver.implicitly_wait(30)
            self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
            self.rp.wx_login('xd153', 'abc123')
            names = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='router_desc']")))
            right_list_base = self.rp.wx_investor_power_list(role)
            right_list = right_list_base.copy()
            lists = []
            for i in names:
                a = i.text
                lists.append(a)
            if right_list == lists:
                print('所有权限:', role + "权限正确", right_list)
            else:
                print('所有权限:', role + "权限错误", '\n', right_list, '\n', lists)
            # self.rp.wx_logout()

    @unittest.skip('不执行')
    # 出资人权限-无提现权限-目前写死权限不受提现影响
    # 【管理员】机柜管理，订单管理，收益统计，提现，数据概况，数据分析，设置
    def test_012(self):
        url = 'http://debug2.wegui.cn/v1/users/MCenqjtx4R'
        role_list = ['main']
        for role in role_list:
            # 布尔值 web（后台登陆）,wxadmin（微信管理端），withdraw（提现）
            data = self.rp.wx_investor_power(role, True, True, False)
            requests.put(url, data=data, headers=self.rp.web_headers())
            self.driver.implicitly_wait(30)
            self.rp.open_url("http://wxadmin.wegui.cn/admin/#/")
            self.rp.wx_login('xd153', 'abc123')
            names = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='router_desc']")))
            right_list_base = self.rp.wx_investor_power_list(role)
            right_list = right_list_base.copy()
            if '提现' in right_list:
                right_list.remove('提现')
                lists = []
                for i in names:
                    a = i.text
                    lists.append(a)
                if right_list == lists:
                    print('关闭数据统计权限:', role + "权限正确", right_list)
                else:
                    print('关闭数据统计权限:', role + "权限错误", '\n', right_list, '\n', lists)
                self.rp.wx_logout()

    @unittest.skip('不执行')
    # 区域经理权限
    # 【管理员】
    # 【运维员】
    # 【财务员】
    # 【总营收管理员】
    # 【分成管理员】
    def test_013(self):
        pass


if __name__ == '__main__':
    unittest.main()