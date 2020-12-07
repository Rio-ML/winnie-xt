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
        print("测试用例执行完成")
        pass

    def setUp(self):
        self.rp = RegisterPage(self)
        self.st = SessionToken()
        self.ko = KDGOrder()

    def tearDown(self):
        pass

    # @unittest.skip('不执行')
    # 快递员投件：1.给已注册用户投件不扣除短信费用4，重新发送取件码扣费6
    # 2.给未注册用户投件扣除短信费用5，重新发送取件码再次扣费6
    # 3.更改手机号为已注册用户不扣短信费用7，更改为未注册用户扣除短信费用8
    # 4.取消投件扣除短信费用 1，2
    # 5.管理后台-发送取件码扣费 3
    # 6.水帘洞网点开启不允许欠费，管理后台重新发送取件码不能成功9，微信管理端重发取件码不可成功10
    # 7.水帘洞网点开启不允许欠费，更改为未注册用户不可成功11
    def test01_message_deduction(self):
        # 取消投件扣除短信费用
        # 设置水帘洞网点可欠费
        self.ko.saas_not_allow_arrears('水帘洞网点', arrears_status=False)
        # 下单
        self.ko.YT_occupy('z012009428143', prohibit=())
        order = self.ko.KDG_order('z012009428143', 3, '18707175056', '22334455667789', lockerType="m")
        # print(order)
        order_id = order['objectId']
        # print(order_id)
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        print(site_account_before)
        # 微信端取消订单-开门-发送短信-扣除短信费用
        self.ko.KDG_close_order_open_door(order_id)
        site_account_after = self.ko.site_shop_account("南天门合作商")
        print(site_account_after)
        if site_account_before-site_account_after == 35:
            print('测试通过-取消投件扣除短信费用-开门')
        else:
            print('测试不通过-取消投件扣除短信费用-开门')

    def test02_message_deduction(self):
        # 取消投件扣除短信费用
        # 下单
        self.ko.YT_occupy('z012009428143', prohibit=())
        order = self.ko.KDG_order('z012009428143', 3, '18707175056', '22334455667790', lockerType="m")
        print(order)
        order_id = order['objectId']
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        # 微信端取消订单-不开门-发送短信-扣除短信费用
        self.ko.KDG_close_order_close_door(order_id)
        site_account_after = self.ko.site_shop_account("南天门合作商")
        if site_account_before-site_account_after == 35:
            print('测试通过-取消投件扣除短信费用-不开门')
        else:
            print('测试不通过-取消投件扣除短信费用-不开门')

    def test03_message_deduction(self):
        # 管理后台-发送取件码扣费
        # 下单
        self.ko.YT_occupy('z012009428143', prohibit=())
        order = self.ko.KDG_order('z012009428143', 3, '18707175056', '22334455667790', lockerType="m")
        order_id = order['objectId']
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        # 管理后台-发送取件码扣费
        self.ko.saas_send_code(order_id)
        site_account_after = self.ko.site_shop_account("南天门合作商")
        # 管理后台关闭订单
        self.ko.saas_close_order(order_id=order_id)
        if site_account_before-site_account_after == 35:
            print('测试通过-管理后台-发送取件码扣费')
        else:
            print('测试不通过-管理后台-发送取件码扣费')

    def test04_message_deduction(self):
        # 给已注册用户投件不扣除短信费用
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        # 下单
        self.ko.YT_occupy('z012009428143', prohibit=())
        order = self.ko.KDG_order('z012009428143', 3, '18707175056', '22334455667790', lockerType="m")
        order_id = order['objectId']
        site_account_after = self.ko.site_shop_account("南天门合作商")
        # 管理后台关闭订单
        self.ko.saas_close_order(order_id=order_id)
        if site_account_before - site_account_after == 0:
            print('测试通过-给已注册用户投件不扣费')
        else:
            print('测试不通过-给已注册用户投件不扣费')

    def test05_message_deduction(self):
        # 给未注册用户投件扣除短信费用
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        # 下单
        self.ko.YT_occupy('z012009428143', prohibit=())
        order = self.ko.KDG_order('z012009428143', 3, '13410356712', '22334455667790', lockerType="m")
        order_id = order['objectId']
        site_account_after = self.ko.site_shop_account("南天门合作商")
        # 管理后台关闭订单
        self.ko.saas_close_order(order_id=order_id)
        if site_account_before - site_account_after == 35:
            print('测试通过-给已注册用户投件不扣费')
        else:
            print('测试不通过-给已注册用户投件不扣费')

    def test06_message_deduction(self):
        # 重新发送取件码扣费
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        # 下单
        self.ko.YT_occupy('z012009428143', prohibit=())
        order = self.ko.KDG_order('z012009428143', 3, '18707175056', '22334455667790', lockerType="m")
        order_id = order['objectId']
        # 重发验证码-扣除短信费用
        self.ko.KDG_send_code(order_id)
        site_account_after = self.ko.site_shop_account("南天门合作商")
        # 管理后台关闭订单
        self.ko.saas_close_order(order_id=order_id)
        if site_account_before - site_account_after == 35:
            print('测试通过-给已注册用户投件不扣费')
        else:
            print('测试不通过-给已注册用户投件不扣费')

    def test07_message_deduction(self):
        # 更改手机号为已注册用户不扣短信费用
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        # 下单
        self.ko.YT_occupy('z012009428143', prohibit=())
        order = self.ko.KDG_order('z012009428143', 3, '18707175056', '22334455667790', lockerType="m")
        order_id = order['objectId']
        # 更改手机号为已注册用户
        self.ko.KDG_update_phone(order_id, '17879508562')
        site_account_after = self.ko.site_shop_account("南天门合作商")
        # 管理后台关闭订单
        self.ko.saas_close_order(order_id=order_id)
        if site_account_before - site_account_after == 0:
            print('测试通过-更改手机号为已注册用户不扣费')
        else:
            print('测试不通过-更改手机号为已注册用户不扣费')

    def test08_message_deduction(self):
        # 更改手机号为未注册用户扣除短信费用
        # 获取合作商账户余额
        site_account_before = self.ko.site_shop_account("南天门合作商")
        # 下单
        self.ko.YT_occupy('z012009428143', prohibit=())
        order = self.ko.KDG_order('z012009428143', 3, '18707175056', '22334455667790', lockerType="m")
        order_id = order['objectId']
        # 更改手机号为未注册用户
        self.ko.KDG_update_phone(order_id, '13410356712')
        site_account_after = self.ko.site_shop_account("南天门合作商")
        # 管理后台关闭订单
        self.ko.saas_close_order(order_id=order_id)
        if site_account_before - site_account_after == 35:
            print('测试通过-更改手机号为未注册用户扣费')
        else:
            print('测试不通过-更改手机号为未注册用户扣费')

    def test09_message_deduction(self):
        # 管理后台-发送取件码扣费-不成功
        # 设置水帘洞网点可欠费
        self.ko.saas_not_allow_arrears('水帘洞网点', arrears_status=False)
        # 下单
        self.ko.YT_occupy('z012009428143', prohibit=())
        order = self.ko.KDG_order('z012009428143', 3, '18707175056', '22334455667790', lockerType="m")
        order_id = order['objectId']
        # 设置水帘洞网点不可欠费
        self.ko.saas_not_allow_arrears('水帘洞网点', arrears_status=True)
        # 管理后台-发送取件码扣费
        res = self.ko.saas_send_no_code(order_id)
        # 管理后台关闭订单
        self.ko.saas_close_order(order_id=order_id)
        if res['message'] == '参数错误:当前设备因运营商问题无法再次发送短信,请联系小铁客服处理!':
            print('测试通过-网点不可欠费-管理后台发送取件码不成功')
        else:
            print('测试不通过-网点不可欠费-管理后台发送取件码不成功')

    def test10_message_deduction(self):
        # 网点不可欠费-重新发送取件码扣费-不成功
        # 设置水帘洞网点可欠费
        self.ko.saas_not_allow_arrears('水帘洞网点', arrears_status=False)
        # 下单
        self.ko.YT_occupy('z012009428143', prohibit=())
        order = self.ko.KDG_order('z012009428143', 3, '18707175056', '22334455667790', lockerType="m")
        order_id = order['objectId']
        # 设置水帘洞网点不可欠费
        self.ko.saas_not_allow_arrears('水帘洞网点', arrears_status=True)
        # 重发验证码-扣除短信费用
        res = self.ko.saas_send_no_code(order_id)
        # 管理后台关闭订单
        self.ko.saas_close_order(order_id=order_id)
        if res['message'] == '参数错误:当前设备因运营商问题无法再次发送短信,请联系小铁客服处理!':
            print('测试通过-网点不可欠费-重新发送取件码不成功')
        else:
            print('测试不通过-网点不可欠费-重新发送取件码不成功')

    def test11_message_deduction(self):
        # 网点不可欠费-手机号更改为未注册用户-不成功
        # 设置水帘洞网点可欠费
        self.ko.saas_not_allow_arrears('水帘洞网点', arrears_status=False)
        # 下单
        self.ko.YT_occupy('z012009428143', prohibit=())
        order = self.ko.KDG_order('z012009428143', 3, '18707175056', '22334455667790', lockerType="m")
        order_id = order['objectId']
        # 设置水帘洞网点不可欠费
        self.ko.saas_not_allow_arrears('水帘洞网点', arrears_status=True)
        # 更改手机号为未注册用户
        res = self.ko.KDG_update_phone(order_id, '13410356712')
        # 管理后台关闭订单
        self.ko.saas_close_order(order_id=order_id)
        if res['message'] == '参数错误:当前设备因运营商问题无法再次发送短信,请联系小铁客服处理!':
            print('测试通过-网点不可欠费-手机号更改为未注册用户不成功')
        else:
            print('测试不通过-网点不可欠费-手机号更改为未注册用户不成功')


if __name__ == '__main__':
    i = 1
    for i in range(1, 2):
        suite = unittest.TestSuite()
        suite.addTest(Verify_Apps1("test01_click_pick_return"))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        time.sleep(2)

