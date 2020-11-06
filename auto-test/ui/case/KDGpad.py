# -*- coding:utf-8 -*-
import unittest
import time
import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport
import requests
import json
import HTMLTestRunner


# def click_down(num):
#     self.d(resourceId="com.motern.cherry.monitor:id/btn_code_confirm").click()
#     c_map={"queding":"btn_code_confirm"}
#     self.d(resourceId="com.motern.cherry.monitor:id/" + c_map[num] + '"').click()

class Verify_Apps1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = u2.connect('12345678')
        # hrp = htmlreport.HTMLReport(cls.d, 'report')
        # hrp.patch_click()
        cls.d.toast.show('测试开始', 3)

    @classmethod
    def tearDownClass(cls):
        # cls.d.app_stop("com.motern.cherry.monitor")
        # cls.d.app_start("com.motern.cherry.monitor")
        cls.d.toast.show('测试结束', 3)

    def setUp(self):
        # self.d = u2.connect('G7FXO1VIAN')
        # hrp = htmlreport.HTMLReport(cls.d, 'report')
        # hrp.patch_click()
        # self.d.toast.show('测试开始', 3)
        pass

    def tearDown(self):
        # self.d.toast.show('测试结束', 3)
        # print("测试错误")
        pass

    # 点击取件，再点击返回
    def test01_click_pick_return(self):
        # v10点击刷新
        self.d(resourceId="com.motern.cherry.monitor:id/rl_refresh").click()
        time.sleep(1)
        for i in range(1, 1000):
            i += 1
            # 点击快递员
            # self.d(resourceId="com.motern.cherry.monitor:id/welcome_btn").click()
            # time.sleep(0.1)
            # 快递员/取件界面点击返回
            # self.d(resourceId="com.motern.cherry.monitor:id/btn_return").click()
            # time.sleep(0.1)
            # 点击取件
            self.d(resourceId="com.motern.cherry.monitor:id/authority_code_btn").click()
            time.sleep(0.1)
            # 快递员/取件界面点击返回
            self.d(resourceId="com.motern.cherry.monitor:id/btn_return").click()
            time.sleep(0.1)
            print(i)


    # #按时收费，开门次数为0，只有一个单
    # def test02_Verify_anshi(self):
    #     #存取包公用sessionToken：Xi-Session-Token从数据库拿user的objectId字段对应session的user字段找到sessionToken未过期的值
    #     login_Xi_Session_Token = 'r:968f79b0078368c1a1a5c61736d6bbcb'
    #     Xi_Session_Token = 'r:175c27400ed59b9f792775e73a1f2fcb'
    #     url_payRule = 'http://debug2.wegui.cn/v1/cabinets/3ZMmzgj7jT/payRule'
    #     url_command = 'http://debug2.wegui.cn/v1/cabinets/3ZMmzgj7jT/commands'
    #     data_payRule = {"forgetPayRule":{"s":{"prepaid":0},"m":{"prepaid":0},"l":{"prepaid":0}},"payRule":{"s":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":0,"perMoney":1,"perTime":60,"prepaid":1,"topMoney":0,"topTime":0,"unlockCount":1,"endTime":0},"m":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":0,"perMoney":0,"perTime":0,"prepaid":0,"topMoney":0,"topTime":0,"unlockCount":1,"endTime":0},"l":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":0,"perMoney":0,"perTime":0,"prepaid":0,"topMoney":0,"topTime":0,"unlockCount":1,"endTime":0}}}
    #     data_command = {"cmd":"update_info","data":{}}
    #     headers={'Content-Type': 'application/json','Xi-App-Id': '0a8020002101b2ddc7626fca179adf70','Xi-Session-Token': login_Xi_Session_Token}
    #     res_payRule = (requests.put(url=url_payRule, data=json.dumps(data_payRule), headers=headers))
    #     res_command = (requests.post(url=url_command, data=json.dumps(data_command), headers=headers))
    #     print(res_command.text)
    #     time.sleep(3)
    #     #header内容
    #     headers={'Content-Type': 'application/json','Xi-App-Id': '0a8020002101b2ddc7626fca179adf70','Xi-Session-Token': Xi_Session_Token}
    #     #微信公众号存包下订单url
    #     order_url = 'https://azapi.wegui.cn/v1/orders'
    #     #请求内容：机柜z011805822625-4号锁 待优化：锁号随机 先编辑计费规则后下订单
    #     data_order = {"cabinetId":"3ZMmzgj7jT","rentType":"short","lockerType":"s","passwordEnable":True,"prepaid":1,"manualLockerEnable":True,"lockerId":"wZi8vFu8Hh","phone":"19977885681","password":"1111"}
    #     #post请求
    #     r = requests.post(order_url,json = data_order,headers = headers)
    #     print(r.text)
    #     # 获取response里的objectId传给取包接口
    #     objectId = r.json()['objectId']
    #     print(objectId)
    #     # 点击“中途开门”
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_get_bag").click()
    #     time.sleep(2)
    #     # 结束寄存
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_over").click()
    #     time.sleep(1)
    #     # 取走全部物品
    #     self.d(resourceId="com.motern.cherry.monitor:id/fg_tc_btn_cancel").click()
    #     # 输入手机号
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_1").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_9").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_9").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_7").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_7").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_8").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_8").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_5").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_6").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_8").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_1").click()
    #     # 输入密码
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_1").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_1").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_1").click()
    #     self.d(resourceId="com.motern.cherry.monitor:id/btn_1").click()
    #     time.sleep(20)


# if __name__ == '__main__':
#     unittest.main()

if __name__ == '__main__':
    i = 1
    for i in range(1, 2):
        suite = unittest.TestSuite()
        suite.addTest(Verify_Apps1("test01_click_pick_return"))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        time.sleep(2)

