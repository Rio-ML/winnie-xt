# -*- coding: utf-8 -*-
from page.register_page import RegisterPage
import time


class RegisterHandle(object):
    def __init__(self, driver):
        self.register_p = RegisterPage(driver)

    # 输入用户名
    def send_user_name(self, user_name):
        self.register_p.get_user_name_element().send_keys(user_name)

    # 输入密码
    def send_user_pwd(self, user_pwd):
        self.register_p.get_user_pwd_element().send_keys(user_pwd)

    # 获取文字信息
    def get_user_text(self, info, user_info):
        try:
            if info == 'user_name_error':
                # text = self.register_p.get_user_name_error_element().get_attribute('value')
                ele = self.register_p.get_user_name_error_element()
                time.sleep(3)
                text = ele.text
            elif info == 'user_pwd_error':
                # text = self.register_p.get_user_pwd_error().get_attribute('value')
                ele = self.register_p.get_user_pwd_error()
                time.sleep(3)
                text = ele.text
            else:
                ele = self.register_p.get_login_error()
                time.sleep(2)
                text = ele.text
        except Exception as e:
            print(e)
            text = None
        return text == user_info

    # 点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    # 获取注册按钮文字
    def get_register_text(self):
        return self.register_p.get_button_element().text

    def click_user_name(self):
        self.register_p.get_user_name_element().click()

    def click_user_pwd(self):
        self.register_p.get_user_pwd_element().click()
