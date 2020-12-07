# -*- coding:utf-8 -*-
import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport
import HTMLTestRunner
import requests
import json
import unittest
import time
from ui.page.element_page import RegisterPage
from ui.page.element_page import SessionToken
from ui.page.KDGpage import PadPage
from api.kdg_api.kdg_order import KDGOrder


class Verify_Apps1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.pp = PadPage('G7FXO2C677')
        self.rp = RegisterPage(self)
        self.st = SessionToken()
        self.ko = KDGOrder()
        self.pp.d.toast.show('测试开始', 3)
        pass

    @classmethod
    def tearDownClass(self):
        # self.pp.d.toast.show('测试结束', 3)
        print('测试完成')
        pass

    def setUp(self):
        # self.pp = PadPage('G7FXO2C677')
        # self.rp = RegisterPage(self)
        # self.st = SessionToken()
        # self.ko = KDGOrder()
        # self.pp.d.toast.show('测试开始', 3)
        pass

    def tearDown(self):
        # self.pp.d.toast.show('测试结束', 3)
        time.sleep(1)
        pass

    # @unittest.skip('不执行')
    # 快递员投件：1.给已注册用户投件不扣除短信费用1
    # 2.给未注册用户投件扣除短信费用2
    # 3.取消投件扣除短信费用3，4
    # 4.开启不允许欠费，投件提示不成功5
    def test01_message_deduction_pad(self):
        # 给已注册用户投件不扣除短信费用
        self.ko.YT_occupy('z012009428143', prohibit=())
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        self.pp.deliver_login('18707175056', '222222')
        self.pp.pad_button("小柜")
        self.pp.pad_input_text("单号", "1122334455")
        self.pp.pad_input_text("收件人手机号", "18707175056")
        self.pp.pad_input_text("二次确认手机号", "18707175056")
        self.pp.pad_button("单号-键盘确定")
        self.pp.pad_button("返回")
        site_account_after = self.ko.site_shop_account("南天门合作商")
        if site_account_before-site_account_after == 0:
            print('测试通过-PAD-给已注册用户投件不扣短信费')
        else:
            print('测试不通过-PAD-给已注册用户投件不扣短信费')
        # 管理后台关闭订单
        self.ko.saas_close_order(phone='18707175056')

    # @unittest.skip('不执行')
    def test02_message_deduction_pad(self):
        # 给未注册用户投件扣除短信费用
        self.ko.YT_occupy('z012009428143', prohibit=())
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        self.pp.deliver_login('18707175056', '222222')
        self.pp.pad_button("小柜")
        self.pp.pad_input_text("单号", "1122334455")
        self.pp.pad_input_text("收件人手机号", "13410356712")
        self.pp.pad_input_text("二次确认手机号", "13410356712")
        self.pp.pad_button("单号-键盘确定")
        self.pp.pad_button("返回")
        site_account_after = self.ko.site_shop_account("南天门合作商")
        if site_account_before-site_account_after == 35:
            print('测试通过-PAD-给未注册用户投件扣短信费')
        else:
            print('测试不通过-PAD-给未注册用户投件扣短信费')
        self.ko.saas_close_order(phone='13410356712')

    def test03_message_deduction_pad(self):
        # 取消投件扣除短信费用-未投件
        self.ko.YT_occupy('z012009428143', prohibit=())
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        self.pp.deliver_login('18707175056', '222222')
        self.pp.pad_button("小柜")
        self.pp.pad_input_text("单号", "1122334455")
        self.pp.pad_input_text("收件人手机号", "18707175056")
        self.pp.pad_input_text("二次确认手机号", "18707175056")
        self.pp.pad_button("单号-键盘确定")
        self.pp.pad_button("投件异常")
        self.pp.pad_button("未投件")
        self.pp.pad_button("投件异常-确定")
        site_account_after = self.ko.site_shop_account("南天门合作商")
        if site_account_before-site_account_after == 35:
            print('测试通过-PAD-取消投件-未投件-扣除短信费用')
        else:
            print('测试不通过-PAD-取消投件-未投件-扣除短信费用')

    def test04_message_deduction_pad(self):
        # 取消投件扣除短信费用-拿出快递
        self.ko.YT_occupy('z012009428143', prohibit=())
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        self.pp.deliver_login('18707175056', '222222')
        self.pp.pad_button("小柜")
        self.pp.pad_input_text("单号", "1122334455")
        self.pp.pad_input_text("收件人手机号", "18707175056")
        self.pp.pad_input_text("二次确认手机号", "18707175056")
        self.pp.pad_button("单号-键盘确定")
        self.pp.pad_button("投件异常")
        self.pp.pad_button("拿出快递")
        self.pp.pad_button("投件异常-确定")
        site_account_after = self.ko.site_shop_account("南天门合作商")
        if site_account_before-site_account_after == 35:
            print('测试通过-PAD-取消投件-拿出快递-扣除短信费用')
        else:
            print('测试不通过-PAD-取消投件-拿出快递-扣除短信费用')

    def test05_message_deduction_pad(self):
        pass


if __name__ == '__main__':
    i = 1
    for i in range(1, 2):
        suite = unittest.TestSuite()
        suite.addTest(Verify_Apps1("test01_click_pick_return"))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        time.sleep(2)

