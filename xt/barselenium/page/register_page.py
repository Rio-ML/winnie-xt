# -*- coding: utf-8 -*-
from base.find_element import FindElement


class RegisterPage(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取输入员工姓名元素
    def get_user_staff_name(self):
        return self.fd.get_element("staff_name")

    # 获取输入员工姓名元素(为空)
    def get_user_staff_name_empty(self):
        return self.fd.get_element("staff_name_empty")

    # 获取输入员工电话元素
    def get_staff_phone(self):
        return self.fd.get_element("staff_phone")

    # 获取选择性别元素
    def get_user_sex(self):
        return self.fd.get_element("user_sex")

    # 获取输入员工民族
    def get_user_national(self):
        return self.fd.get_element("user_national")

    # 获取选择员工生日元素
    def get_user_birth(self):
        return self.fd.get_element("user_birth")

    # 获取输入员工身份证号元素
    def get_user_id(self):
        return self.fd.get_element("user_id")

    # 获取选择身份证地址元素
    def get_user_id_place_select(self):
        return self.fd.get_element("user_id_place_select")

    # 获取输入身份证详细地址元素
    def get_user_id_place_input(self):
        return self.fd.get_element("user_id_place_input")

    # 获取选择现居住地地址元素
    def get_user_live_select(self):
        return self.fd.get_element("user_live_select")

    # 获取输入现居住地详细地址元素
    def get_user_live_input(self):
        return self.fd.get_element("user_live_input")

    # 获取输入紧急联系人姓名元素
    def get_user_contact_name(self):
        return self.fd.get_element("user_contact_name")

    # 获取输入紧急联系人电话元素
    def get_user_contact_phone(self):
        return self.fd.get_element("user_contact_phone")

    # 获取选择职位元素
    def get_user_job(self):
        return self.fd.get_element("user_job")

    # 获取选择提成方式元素
    def get_user_profit(self):
        return self.fd.get_element("user_profit")

    # 获取选择政治面貌元素
    def get_user_politics(self):
        return self.fd.get_element("user_politics")

    # 获取选择学历元素
    def get_user_education(self):
        return self.fd.get_element("user_education")

    # 获取输入毕业院校元素
    def get_user_school(self):
        return self.fd.get_element("user_school")

    # 获取选择毕业日期元素
    def user_graduate_date(self):
        return self.fd.get_element("user_graduate_date")

    # 获取输入身高元素
    def user_height(self):
        return self.fd.get_element("user_height")

    # 获取输入体重元素
    def get_user_weight(self):
        return self.fd.get_element("user_weight")

    # 获取选择血型元素
    def get_user_blood(self):
        return self.fd.get_element("user_blood")

    # 获取点击提交按钮元素
    def get_register_button_element(self):
        return self.fd.get_element("register_button")
