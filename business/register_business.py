# -*- coding: utf-8 -*-f
import time
from handle.get_utils import ActionUtil
from page.element_page import RegisterPage


class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_h = ActionUtil(driver)
        self.driver = driver
        self.rp = RegisterPage(driver)

    def contract_base(self):
        self.driver.implicitly_wait(30)
        time.sleep(1)
        self.rp.open_xt_menu('合同审批(新)')
        self.rp.all_button("添加申请")
        self.rp.input_text("网点名称", "2020061701")
        self.rp.drop_down_box("场景分类", "运动健身")
        self.rp.input_text("联系人", "飞鸟")
        self.rp.input_text("联系电话", "15588889999")
        self.rp.input_text("营业开始时间", "120")
        self.register_h.click("//input[@placeholder='请选择营业开始时间']")
        self.rp.all_button("营业时间-确认")
        self.register_h.click("//input[@placeholder='请选择营业结束时间']")
        self.rp.all_button("营业时间-确认")
        self.rp.input_text("网点地址", "河东狮吼")
        self.rp.input_text("每日营收", "12")
        self.rp.input_text("营业时长", "12")
        self.rp.input_text("场地人流量", "12")
        self.rp.input_text("场地规模", "12")
        self.rp.input_text("收费规则", "12")
        self.rp.input_text("平台分成", "100")
        self.rp.input_text("其它费用", "12")
        time.sleep(1)
        # 滚动
        js = "window.scrollTo(100,1500)"
        self.driver.execute_script(js)
        time.sleep(1)
        self.rp.check_box("其它环境-海边")
        self.rp.all_button("添加柜组")
        self.rp.all_button("添加柜组-主柜加")
        self.rp.all_button("修改柜组-确定")
        self.rp.add_photo("门头照", "E:/xt/xtselenium/util/v.png")
        self.rp.all_button("提交申请")
        self.rp.drop_down_box("请选择审批人", "rwvgkYZmKm")
        self.rp.all_button("请选择审批人-确定")
        # self.rp.all_button(self.driver, "提交成功-确定")


