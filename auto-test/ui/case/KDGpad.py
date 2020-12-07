# -*- coding:utf-8 -*-
import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport
import HTMLTestRunner
import unittest
import time
from ui.page.element_page import RegisterPage
from ui.page.element_page import SessionToken
import requests
import json
from ui.page.KDGpage import PadPage
from api.kdg_api.kdg_order import KDGOrder


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
        self.pp = PadPage('G7FXO2C677')
        self.rp = RegisterPage(self)
        self.st = SessionToken()
        self.ko = KDGOrder()
        self.pp.d.toast.show('测试开始', 3)

    def tearDown(self):
        self.pp.d.toast.show('测试结束', 3)
        # print("测试错误")

    @unittest.skip('不执行')
    # 测试是否又内存溢出，点击刷新-取件-返回
    def test01_click_pick_return(self):
        # v10点击刷新-取件-返回
        self.pp.pad_button("刷新")
        time.sleep(1)
        for i in range(1, 10):
            i += 1
            self.pp.pad_button("取件")
            self.pp.pad_button("返回")
            print(i)

    # @unittest.skip('不执行')
    # 快递员投件：设置圆通占用小柜和中柜，快递员在小柜投递其它快递提示被占用，换成大柜可以投递
    # 点击继续存件，快递员在小柜投递圆通快递，成功
    def test02_deliver_YT_occupy(self):
        # 管理后台设置圆通占用的柜门类型
        self.ko.YT_occupy('z012006664507', prohibit=("s", "m"))
        self.pp.deliver_login('18707175056', '222222')
        self.pp.pad_button("小柜")
        self.pp.pad_input_text("单号", "1122334455")
        self.pp.pad_input_text("收件人手机号", "18707175056")
        self.pp.pad_input_text("二次确认手机号", "18707175056")
        self.pp.pad_button("键盘确认")
        self.pp.pad_button("大柜")
        self.pp.pad_input_text("单号", "1122334455")
        self.pp.pad_input_text("收件人手机号", "18707175056")
        self.pp.pad_input_text("二次确认手机号", "18707175056")
        self.pp.pad_button("键盘确认")
        self.pp.pad_button("继续存件")
        self.pp.pad_button("小柜")
        self.pp.pad_input_text("单号", "YT1122334455")
        self.pp.pad_input_text("收件人手机号", "18707175056")
        self.pp.pad_input_text("二次确认手机号", "18707175056")
        self.pp.pad_button("键盘确认")
        self.pp.pad_button("返回")


if __name__ == '__main__':
    i = 1
    for i in range(1, 2):
        suite = unittest.TestSuite()
        suite.addTest(Verify_Apps1("test01_click_pick_return"))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        time.sleep(2)

