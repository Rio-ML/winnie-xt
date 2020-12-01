# -*- coding:utf-8 -*-
import unittest
import time
import uiautomator2 as u2
from ui.page.element_page import RegisterPage
from ui.page.element_page import SessionToken
import uiautomator2.ext.htmlreport as htmlreport
import requests
import json
from api.Base.runmethod import RunMethod
from api.data import data_config as dc
from api.xt_api.xt_order import XTOrder
import HTMLTestRunner
from ui.page.PADxtpage import PadPage


class Verify_Apps1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.d = u2.connect('G7FXO2C677')
        # cls.rp = PadPage(cls.d)
        # cls.d.toast.show('测试开始', 3)
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.d.toast.show('测试结束', 3)
        pass

    def setUp(self):
        self.pp = PadPage('')
        self.rp = RegisterPage(self)
        self.st = SessionToken()
        self.rm = RunMethod()
        self.xo = XTOrder()
        self.pp.d.toast.show('测试开始', 3)

    def tearDown(self):
        self.pp.d.toast.show('测试结束', 3)
        # print("测试错误")

    # 取件码取包
    @unittest.skip('不执行')
    def test01_pick_code_order(self):
        cab_no = 'z011905751622'
        locker_no = 1
        # 重置手机号
        self.xo.reset_phone("邓～XS Winnie")
        # 配置收费规则 默认按时+不支持密码存包强制输入手机号+长/短租
        self.xo.set_pay_rule(cab_no)
        # 下单
        order_id = self.xo.xt_order(cab_no, locker_no)
        # 获取取件码
        code = self.xo.get_package_code(order_id)
        # pad端操作
        self.pp.pad_button("刷新")
        time.sleep(5)
        self.pp.pad_button("取件码取包")
        self.pp.pad_keyboard(code)
        self.pp.pad_button("键盘-确定")
        # 微信管理端关闭订单
        # self.xo.close_order(order_id)

    # 取件码取包
    # @unittest.skip('不执行')
    def test02_deliver_login(self):
        cab_no = 'z011905751622'
        locker_no = 1
        phone = '18707175056'
        pwd = '5056'
        # 重置手机号
        self.xo.reset_phone("邓～XS Winnie")
        # 配置收费规则 按时+支持密码存包手机号&四位数密码+长/短租
        self.xo.set_pay_rule(cab_no, passwordEnable=True, forcePhoneEnable=False)
        # 下单
        order_id = self.xo.xt_order(cab_no, locker_no, passwordEnable=True, phone=phone, pwd=pwd)
        # pad端操作
        # self.pp.pad_button("刷新")
        # time.sleep(5)
        # self.pp.pad_button("取走物品")
        # self.pp.pad_button("不存了")
        # self.pp.pad_keyboard(phone)
        # self.pp.pad_keyboard(pwd)
        # self.pp.pad_button("键盘-确定")
        # 微信管理端关闭订单
        # self.xo.close_order(order_id)


if __name__ == '__main__':
    i = 1
    for i in range(1, 2):
        suite = unittest.TestSuite()
        suite.addTest(Verify_Apps1("test01_click_pick_return"))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        time.sleep(2)

