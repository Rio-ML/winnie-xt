# -*- coding: utf-8 -*-
from page.register_page import RegisterPage
import time


class RegisterHandle(object):
    def __init__(self, driver):
        self.register_p = RegisterPage(driver)

    # 输入员工姓名
    def send_user_name(self, staff_name):
        self.register_p.get_user_staff_name().send_keys(staff_name)

    # 输入员工电话
    def send_staff_phone(self, staff_phone):
        self.register_p.get_staff_phone().send_keys(staff_phone)

    # 输入员工民族
    def send_staff_national(self, user_national):
        self.register_p.get_staff_phone().send_keys(user_national)

    # 输入员工身份证号
    def send_staff_id(self, user_id):
        self.register_p.get_staff_phone().send_keys(user_id)

    # 输入身份证详细地址
    def send_staff_id_place_input(self, user_id_place_input):
        self.register_p.get_staff_phone().send_keys(user_id_place_input)

    # 输入现居住地详细地址
    def send_staff_live_input(self, user_live_input):
        self.register_p.get_staff_phone().send_keys(user_live_input)

    # 输入紧急联系人姓名
    def send_staff_contact_name(self, user_contact_name):
        self.register_p.get_staff_phone().send_keys(user_contact_name)

    # 输入紧急联系人电话
    def send_contact_phone(self, user_contact_phone):
        self.register_p.get_staff_phone().send_keys(user_contact_phone)

    # 输入毕业院校
    def send_staff_school(self, user_school):
        self.register_p.get_staff_phone().send_keys(user_school)

    # 输入身高
    def send_staff_height(self, user_height):
        self.register_p.get_staff_phone().send_keys(user_height)

    # 输入体重
    def send_staff_weight(self, user_weight):
        self.register_p.get_staff_phone().send_keys(user_weight)

    # 获取文字信息
    def get_user_text(self, info, user_info):
        try:
            if info == 'staff_name_empty':
                # text = self.register_p.get_user_name_error_element().get_attribute('value')
                ele = self.register_p.get_user_staff_name_empty()
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
        self.register_p.get_register_button_element().click()

