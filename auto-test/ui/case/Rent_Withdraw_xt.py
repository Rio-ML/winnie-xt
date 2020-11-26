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

    # @unittest.skip('不执行')
    # 按时+不支持密码存包强制输入手机号,取件码取包
    def test01_pick_code_order(self):
        # 重置手机号
        # self.xo.reset_phone("邓～XS Winnie")
        # 配置收费规则 按时+不支持密码存包强制输入手机号+长/短租
        self.xo.set_pay_rule('z011905751622')
        # 下单
        # order_id = self.xo.xt_order('z011905751622')
        # 获取取件码
        # code = self.xo.get_package_code(order_id)
        # pad端操作
        # self.pp.pad_button("刷新")
        # time.sleep(5)
        # self.pp.pad_button("取件码取包")
        # self.pp.pad_keyboard(code)
        # self.pp.pad_button("键盘-确定")


    @unittest.skip('不执行')
    # 快递员投件：设置圆通占用小柜和中柜，快递员在小柜投递其它快递提示被占用，换成大柜可以投递
    # 点击继续存件，快递员在小柜投递圆通快递，成功
    def test02_deliver_login(self):
        # 管理后台设置圆通占用的柜门类型
        url = 'https://lwd2.wegui.cn/v1/sites/xN3ZvEoioM'
        # {"prohibit":["s","m","l","xs"]}
        data = {"prohibit": ["s", "m"]}
        requests.put(url, data=json.dumps(data), headers=self.st.KDG_web_headers())
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

