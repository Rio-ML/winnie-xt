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
        pass

    # 各种按钮
    def pad_button(self, a_button):
        class_map = {
            "刷新": '//*[@resource-id="com.motern.cherry.monitor:id/rl_refresh"]/android.widget.ImageView[1]',
            "取件码取包": '//*[@resource-id="com.motern.cherry.monitor:id/authority_code_btn"]',
            "返回": '//*[@resource-id="com.motern.cherry.monitor:id/btn_return"]',
            "密码取包": '//*[@resource-id="com.motern.cherry.monitor:id/rl_root2"]/android.widget.RelativeLayout[6]',
            "键盘-删除": '//*[@resource-id="com.motern.cherry.monitor:id/btn_cancel"]',
            "键盘-确定": '//*[@resource-id="com.motern.cherry.monitor:id/btn_code_confirm"]'
        }
        assert a_button in class_map
        self.d.xpath(class_map[a_button]).click()
        # self.d(resourceId=class_map[a_button]).click()

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
        self.d.xpath(class_map[location_box]).click()
        self.d.send_keys(value, clear=True)

    # 键盘
    def pad_keyboard(self, value):
        class_map = {
            "1": '//*[@resource-id="com.motern.cherry.monitor:id/btn_1"]',
            "2": '//*[@resource-id="com.motern.cherry.monitor:id/btn_2"]',
            "3": '//*[@resource-id="com.motern.cherry.monitor:id/btn_3"]',
            "4": '//*[@resource-id="com.motern.cherry.monitor:id/btn_4"]',
            "5": '//*[@resource-id="com.motern.cherry.monitor:id/btn_5"]',
            "6": '//*[@resource-id="com.motern.cherry.monitor:id/btn_6"]',
            "7": '//*[@resource-id="com.motern.cherry.monitor:id/btn_7"]',
            "8": '//*[@resource-id="com.motern.cherry.monitor:id/btn_8"]',
            "9": '//*[@resource-id="com.motern.cherry.monitor:id/btn_9"]',
            "0": '//*[@resource-id="com.motern.cherry.monitor:id/btn_0"]'
        }
        a = list(value)
        for i in a:
            self.d.xpath(class_map[i]).click()


if __name__ == '__main__':
    d = PadPage('')

