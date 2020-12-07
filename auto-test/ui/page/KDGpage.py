# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import json
import requests
from ui.util.DriverInit import DriverInit
import uiautomator2 as u2
from ui.handle.get_utils import ActionUtil


class PadPage(object):
    def __init__(self, serial):
        self.d = u2.connect(serial)

    # 登陆
    def deliver_login(self, username, password):
        PadPage.pad_button(self, "快递员")
        PadPage.pad_button(self, "终端投件")
        PadPage.pad_keyboard(self, username)
        PadPage.pad_keyboard(self, password)
        PadPage.pad_button(self, "键盘确认")
        PadPage.pad_button(self, "快速投件")

    # 各种按钮
    def pad_button(self, a_button):
        class_map = {
            "刷新": '//*[@resource-id="com.motern.cherry.monitor:id/include"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]',
            "取件": "com.motern.cherry.monitor:id/authority_code_btn",
            "快递员": "com.motern.cherry.monitor:id/welcome_btn",
            "终端投件": "com.motern.cherry.monitor:id/btn_rent",
            "快速投件": "com.motern.cherry.monitor:id/btn_fast_push",
            "键盘确认": "com.motern.cherry.monitor:id/btn_code_confirm",
            "单号-键盘确定": "com.motern.cherry.monitor:id/ok",
            "微小柜": "com.motern.cherry.monitor:id/btn_xsmall",
            "小柜": "com.motern.cherry.monitor:id/btn_small",
            "中柜": "com.motern.cherry.monitor:id/btn_mid",
            "大柜": "com.motern.cherry.monitor:id/btn_big",
            "投件异常": "com.motern.cherry.monitor:id/error",
            "大小不合适": "com.motern.cherry.monitor:id/btn_change_locker",
            "门未开": "com.motern.cherry.monitor:id/btn_change_locker2",
            "再开一次": "com.motern.cherry.monitor:id/btn_re_open",
            "未投件": "com.motern.cherry.monitor:id/btn_cancel_order",
            "拿出快递": "com.motern.cherry.monitor:id/btn_cancel_order2",
            "投件异常-确定": "com.motern.cherry.monitor:id/btn_ok",
            "投件异常-取消": "com.motern.cherry.monitor:id/btn_cancel",
            "返回": "com.motern.cherry.monitor:id/btn_return"
        }
        assert a_button in class_map
        self.d.implicitly_wait(20)
        if a_button == "刷新":
            self.d.xpath(class_map[a_button]).click(timeout=10)
        else:
            self.d(resourceId=class_map[a_button]).click()

    # 各种输入框
    def pad_input_text(self, location_box, value):
        class_map = {
            "快递员登陆手机号": "com.motern.cherry.monitor:id/et_phone",
            "快递员登陆密码": "com.motern.cherry.monitor:id/et_pwd",
            "单号": "com.motern.cherry.monitor:id/et_orderId",
            "收件人手机号": "com.motern.cherry.monitor:id/et_phone",
            "二次确认手机号": "com.motern.cherry.monitor:id/et_re_phone"
        }
        assert location_box in class_map
        self.d(resourceId=class_map[location_box]).click()
        self.d.send_keys(value, clear=True)

    # # 各种弹框确认----待完善
    # def alert_check(self, xpath, alert_title, yes_or_no):
    #     class_map = {
    #         "是否继续填写上次保存的申请？": "//div[text()='是否继续填写上次保存的申请？']"
    #     }
    #     class_map1 = {
    #         "否，删除记录": "//div[text()='否，删除记录']",
    #         "是，继续": "//div[text()='是，继续']"
    #     }
    #     assert alert_title in class_map
    #     assert yes_or_no in class_map1
    #     if self.register_h.get_attribute(xpath, class_map[alert_title]):
    #         self.register_h.click(class_map1[yes_or_no])

    # 键盘
    def pad_keyboard(self, value):
        class_map = {
            "1": "com.motern.cherry.monitor:id/btn_1",
            "2": "com.motern.cherry.monitor:id/btn_2",
            "3": "com.motern.cherry.monitor:id/btn_3",
            "4": "com.motern.cherry.monitor:id/btn_4",
            "5": "com.motern.cherry.monitor:id/btn_5",
            "6": "com.motern.cherry.monitor:id/btn_6",
            "7": "com.motern.cherry.monitor:id/btn_7",
            "8": "com.motern.cherry.monitor:id/btn_8",
            "9": "com.motern.cherry.monitor:id/btn_9",
            "0": "com.motern.cherry.monitor:id/btn_0",
            "取消": "com.motern.cherry.monitor:id/btn_cancel"
        }
        a = list(value)
        for i in a:
            self.d(resourceId=class_map[i]).click()

    # # 文案检查----待完善
    # def text_check(self, location_box, value):
    #     class_map = {
    #         "取件单号": "com.motern.cherry.monitor:id/order_num",
    #         "取件号码": "com.motern.cherry.monitor:id/order_phone",
    #         "打开柜门": "com.motern.cherry.monitor:id/locker_name",
    #     }
    #     assert location_box in class_map
    #     self.register_h.input(class_map[location_box], value)


if __name__ == '__main__':
    d = PadPage('G7FXO2C677')

