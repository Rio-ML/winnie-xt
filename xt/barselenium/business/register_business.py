# -*- coding: utf-8 -*-f
from handle.register_handle import RegisterHandle
import time


class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, user_name, staff_phone, national, staff_id, id_place_input, live_input, contact_name, contact_phone, height, weight):
        # self.register_h.register_p.implicitly_wait(3)
        self.register_h.send_user_name(user_name)
        time.sleep(2)
        self.register_h.send_staff_phone(staff_phone)
        time.sleep(2)
        self.register_h.send_staff_national(national)
        time.sleep(2)
        self.register_h.send_staff_id(staff_id)
        time.sleep(2)
        self.register_h.send_staff_id_place_input(id_place_input)
        time.sleep(2)
        self.register_h.send_staff_live_input(live_input)
        time.sleep(2)
        self.register_h.send_staff_contact_name(contact_name)
        time.sleep(2)
        self.register_h.send_contact_phone(contact_phone)
        time.sleep(2)
        self.register_h.send_staff_height(height)
        time.sleep(2)
        self.register_h.send_staff_weight(weight)
        time.sleep(2)
        self.register_h.click_register_button()

    def register_success(self):
        if self.register_h.get_user_text() == None:
            return True
        else:
            return False

    # 执行操作
    def login_user_name_error(self, user_name, user_pwd):
        self.user_base(user_name, user_pwd)
        if self.register_h.get_user_text('user_name_error', "请输入账号"):
            # print("用户名填写错误")
            return True
        else:
            return False

    def login_user_pwd_error(self, user_name, user_pwd):
        self.user_base(user_name, user_pwd)
        if self.register_h.get_user_text('user_pwd_error', "请输入密码"):
            # print("密码检验不成功")
            return True
        else:
            return False

    def login_fail(self, user_name, user_pwd):
        self.user_base(user_name, user_pwd)
        if self.register_h.get_user_text('login_fail', "登录失败"):
            # print("密码检验不成功")
            return True
        else:
            return False

