# -*- coding:utf-8 -*-
from selenium.webdriver.support.select import Select

from handle.get_utils import *


class RegisterPage(object):

    # 登陆
    def login(self, driver, username, password):
        Action_util.Input(driver, "//input[@placeholder='用户名']", username)
        Action_util.Input(driver, "//input[@placeholder='密码']", password)
        Action_util.Click(driver, "//button[@class='mint-button primary-btn mint-button--default mint-button--large']")

    # 各种按钮
    def all_button(self, driver, a_button):
        class_map = {
            "添加申请": "//span[text()='添加申请']/parent::*/parent::*",
            "提交申请": "//button[text()='提交申请']/parent::*",
            "保存": "//button[text()='保存']/parent::*",
            "营业时间-确认": "//button[@class='van-picker__confirm']",
            "提交申请确定": "//div[text()='确定']/preceding-sibling::div[text()='保存成功']/following-sibling::div[text()='确定']",
            "添加柜组": "//button[@class='btn-small']",
            "添加柜组-主柜加": "//td[text()='主柜']/parent::*/td/div/div[3]",
            "修改柜组-确定": "//div[text()='- 修改柜组 -']/parent::*/div[text()='确定']",
            "请选择审批人-确定": "//div[text()='- 请选择审批人 -']/parent::*/div[text()='确定']",
            "请选择审批人-取消": "//div[text()='- 请选择审批人 -']/parent::*/div[text()='取消']",
            "提交成功-确定": "//div[text()='提交成功']/parent::*/div[@class='mask-btn' and text()='确定']"
        }
        assert a_button in class_map
        Action_util.Click(driver, class_map[a_button])

    # 各种输入框
    def input_text(self, driver, location_box, value):
        class_map = {
            "网点名称": "//input[@placeholder='请输入网点名称']",
            "联系人": "//input[@placeholder='请输入联系人']",
            "联系电话": "//input[@placeholder='请输入联系电话']",
            "营业开始时间": "//input[@placeholder='请选择营业开始时间']",
            "营业结束时间": "//input[@placeholder='请选择营业结束时间']",
            "网点地址": "//input[@placeholder='详细地址']",
            "每日营收": "//input[@placeholder='预计平均每日营收']",
            "营业时长": "//input[@placeholder='每年营业多少个月']",
            "场地人流量": "//input[@placeholder='平均每日人流量']",
            "场地规模": "//input[@placeholder='请输入场地规模']",
            "收费规则": "//input[@placeholder='请输入收费规则']",
            "平台分成": "//input[@id='openTime']",
            "商户分成": "//input[@id='closeTime']",
            "其它分成": "//input[@placeholder='请注明']",
            "其它费用": "//input[@placeholder='搬运费、打包等']",
            "备注": "//textarea[@class='textarea']"
        }
        assert location_box in class_map
        Action_util.Input(driver, class_map[location_box], value)

    # 各种下拉框选择
    def drop_down_box(self, driver, loc_select, value):
        class_map = {
            "场景分类": "//div[text()='场景分类：']/parent::*/div/select",
            "网点类型": "//div[text()='网点类型：']/parent::*/div/select",
            "合作模式": "//div[text()='合作模式：']/parent::*/div/select",
            "放柜环境": "//div[text()='放柜环境：']/parent::*/div/select",
            "柜子颜色": "//div[text()='柜子颜色：']/parent::*/div/select",
            "请选择审批人": "//select[@placeholder='请选择审批人']"
        }
        assert loc_select in class_map
        Select(driver.find_element_by_xpath(class_map[loc_select])).select_by_value(value)

    # 各种勾选框
    def check_box(self, driver, check_or_not):
        class_map = {
            "需扣除运费": "//input[@id='needFreight']",
            "需扣除贴纸费用": "//input[@id='needSticker']",
            "需扣除人工费用": "//input[@id='needLabor']",
            "其它环境-海边": "//input[@id='oceanEnable']",
            "其它环境-地面有积水": "//input[@id='waterEnable']",
            "所需配件-定制贴纸": "//input[@id='paperEnable']",
            "所需配件-定制雨棚": "//input[@id='canopyEnable']",
            "所需配件-脚杯": "//input[@id='footCupEnable']",
            "所需配件-轮子": "//input[@id='wheelEnable']",
        }
        assert check_or_not in class_map
        Action_util.Click(driver, class_map[check_or_not])

    # 各种弹框确认
    def alert_check(self, driver, xpath, alert_title, yes_or_no):
        class_map = {
            "是否继续填写上次保存的申请？": "//div[text()='是否继续填写上次保存的申请？']"
        }
        class_map1 = {
            "否，删除记录": "//div[text()='否，删除记录']",
            "是，继续": "//div[text()='是，继续']"
        }
        assert alert_title in class_map
        assert yes_or_no in class_map1
        if Action_util.Get_attribute(driver, xpath, class_map[alert_title]):
            Action_util.Click(driver, class_map1[yes_or_no])

    # 添加图片
    def add_photo(self, driver, xpath, photo):
        class_map = {
            "门头照": "//input[@type='file']"
        }
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, class_map[xpath]))).send_keys(photo)

    # 小铁工具的menu
    def open_xt_menu(self, driver, menu=None):
        Action_util.Click(driver, "//div[text()='" + menu + "']/parent::*/parent::*")
