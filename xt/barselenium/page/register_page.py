# -*- coding: utf-8 -*-
from base.find_element import FindElement


class RegisterPage(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取用户名元素
    def get_user_name_element(self):
        return self.fd.get_element("user_name")

    # 获取密码元素
    def get_user_pwd_element(self):
        return self.fd.get_element("user_pwd")

    # 获取错误提示元素
    def get_user_name_error_element(self):
        return self.fd.get_element("user_name_error")

    def get_user_pwd_error(self):
        return self.fd.get_element("user_pwd_error")

    # 获取点击事件元素
    def get_button_element(self):
        return self.fd.get_element("register_confirm_button")

    # 登录失败
    def get_login_error(self):
        return self.fd.get_element("login_fail")
