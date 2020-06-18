# -*- coding: utf-8 -*-f
from handle.get_utils import Action_util
from page.element_page import RegisterPage as rp
import time


class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_h = Action_util(driver)

    def contract_base(self):
        self.driver.implicitly_wait(30)
        rp.login(self.driver, 'xiaod', '123456')
        rp.open_xt_menu(self.driver, '合同审批(新)')
        rp.all_button(self.driver, "添加申请")
        rp.input_text(self.driver, "网点名称", "2020061701")
        rp.drop_down_box(self.driver, "场景分类", "运动健身")
        rp.input_text(self.driver, "联系人", "飞鸟")
        rp.input_text(self.driver, "联系电话", "15588889999")
        rp.input_text(self.driver, "营业开始时间", "120")
        Action_util.Click(self.driver, "//input[@placeholder='请选择营业开始时间']")
        rp.all_button(self.driver, "营业时间-确认")
        Action_util.Click(self.driver, "//input[@placeholder='请选择营业结束时间']")
        rp.all_button(self.driver, "营业时间-确认")
        rp.input_text(self.driver, "网点地址", "河东狮吼")
        rp.input_text(self.driver, "每日营收", "12")
        rp.input_text(self.driver, "营业时长", "12")
        rp.input_text(self.driver, "场地人流量", "12")
        rp.input_text(self.driver, "场地规模", "12")
        rp.input_text(self.driver, "收费规则", "12")
        rp.input_text(self.driver, "平台分成", "100")
        rp.input_text(self.driver, "其它费用", "12")
        time.sleep(3)
        # 滚动
        js = "window.scrollTo(100,1500)"
        self.driver.execute_script(js)
        time.sleep(3)
        rp.check_box(self.driver, "其它环境-海边")
        rp.all_button(self.driver, "添加柜组")
        rp.all_button(self.driver, "添加柜组-主柜加")
        rp.all_button(self.driver, "修改柜组-确定")
        rp.add_photo(self.driver, "门头照", "E:/xt/xtselenium/util/v.png")
        rp.all_button(self.driver, "提交申请")
        rp.drop_down_box(self.driver, "请选择审批人", "rwvgkYZmKm")
        rp.all_button(self.driver, "请选择审批人-确定")
        rp.all_button(self.driver, "提交成功-确定")


