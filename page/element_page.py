# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from handle.get_utils import ActionUtil


class RegisterPage(object):
    def __init__(self, driver):
        self.register_h = ActionUtil(driver)
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    # 登陆
    def wx_login(self, username, password):
        self.register_h.input("//input[@placeholder='用户名']", username)
        self.register_h.input("//input[@placeholder='密码']", password)
        self.register_h.click("//button[@class='mint-button primary-btn mint-button--default mint-button--large']")

    def web_login(self, username, password):
        self.register_h.input("//input[@placeholder='登陆账号']", username)
        self.register_h.input("//input[@placeholder='请输入密码']", password)
        self.register_h.click("//span[text()='确定']")

    # 各种按钮
    def wx_button(self, a_button):
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
        self.register_h.click(class_map[a_button])

    def web_button(self, a_button, shop=None):
        if shop is None:
            shop = ''
        class_map = {
            "添加优惠券": "//button[@type='button']/span[text()='添加优惠券']",
            "优惠券类型": "//input[@placeholder='请选择vip类型']",
            "普通优惠券": "//span[text()='普通优惠券']",
            "vip券": "//span[text()='vip券']",
            "抵扣类型": "//label[text()='抵扣类型']/following-sibling::*/div",
            "普通-抵扣现金": "//span[text()='抵扣现金']",
            "vip券-抵扣现金": "//span[text()='vip券']/ancestor::*[5]/following-sibling::*/div/div/ul/li/span[text()='抵扣现金']",
            "日通票": "//span[text()='日通票']",
            "抵扣时长": "//span[text()='抵扣时长']",
            "所属商户": "//input[@placeholder='请选择所属商户']",
            "商户": "//span[text()='" + shop + "']",
            "状态": "//label[text()='状态']/following-sibling::*/div",
            "上架": "//span[text()='上架']",
            "下架": "//span[text()='下架']",
            "添加优惠券-确定": "//div[@aria-label='添加优惠券']/div/div/button/span[text()='确 定']"
        }
        assert a_button in class_map
        self.register_h.click(class_map[a_button])

    # 各种输入框
    def wx_input_text(self, location_box, value):
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
        self.register_h.input(class_map[location_box], value)

    def web_input_text(self, location_box, value):
        class_map = {
            "优惠券名称": "//label[text()='优惠券名称']/following-sibling::*/div/input",
            "简介": "//label[text()='简介']/following-sibling::*/div/input",
            "面值": "//label[text()='面值']/parent::*/div/div",
            "售价": "//label[text()='售价']/following-sibling::*/div",
            "库存": "//label[text()='库存']/following-sibling::*/div",
            "可抵扣次数": "//label[text()='可抵扣次数']/following-sibling::*/div",
            "备注": "//label[text()='备注']/following-sibling::*/div",
            "抵扣时长": "//label[text()='抵扣时长']/following-sibling::*/div",
            "vip等级": "//label[text()='vip等级']/following-sibling::*/div/input"
        }
        assert location_box in class_map
        self.register_h.input(class_map[location_box], value)

    # 各种下拉框选择
    def drop_down_box(self, loc_select, value):
        class_map = {
            "场景分类": "//div[text()='场景分类：']/parent::*/div/select",
            "网点类型": "//div[text()='网点类型：']/parent::*/div/select",
            "合作模式": "//div[text()='合作模式：']/parent::*/div/select",
            "放柜环境": "//div[text()='放柜环境：']/parent::*/div/select",
            "柜子颜色": "//div[text()='柜子颜色：']/parent::*/div/select",
            "请选择审批人": "//select[@placeholder='请选择审批人']"
        }
        assert loc_select in class_map
        Select(self.driver.find_element_by_xpath(class_map[loc_select])).select_by_value(value)

    # 各种勾选框
    def check_box(self, check_or_not):
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
        self.register_h.click(class_map[check_or_not])

    # 各种弹框确认
    def alert_check(self, xpath, alert_title, yes_or_no):
        class_map = {
            "是否继续填写上次保存的申请？": "//div[text()='是否继续填写上次保存的申请？']"
        }
        class_map1 = {
            "否，删除记录": "//div[text()='否，删除记录']",
            "是，继续": "//div[text()='是，继续']"
        }
        assert alert_title in class_map
        assert yes_or_no in class_map1
        if self.register_h.get_attribute(xpath, class_map[alert_title]):
            self.register_h.click(class_map1[yes_or_no])

    # 添加图片
    def add_photo(self, xpath, photo):
        class_map = {
            "门头照": "//input[@type='file']"
        }
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, class_map[xpath]))).send_keys(photo)

    # 微信管理端 小铁工具的menu
    def open_xt_menu(self, menu):
        self.register_h.click("//div[text()='" + menu + "']/parent::*/parent::*")

    # 后台管理的menu
    def open_web_menu(self, menu):
        self.register_h.click("//span[@title='" + menu + "']")