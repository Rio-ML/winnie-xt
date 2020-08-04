# -*- coding:utf-8 -*-

from selenium import webdriver
import time


class ReserveOperation(object):
    def __init__(self, driver):
        self.driver = driver

    # 仲夏夜之梦
    def reserve_deposit_table_customer(self):
        self.driver.find_element_by_xpath("//div[@class='xi-table-name' and contains(text(),'仲夏夜之梦')]").click()
        self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'订台')]").click()
        # 验证取消按钮是否有效
        self.driver.find_element_by_xpath(
            "//div[@class='drawer']/div[5]/div/div/button/span[contains(text(),'取消')]").click()
        self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'订台')]").click()
        # 顾客订台
        time.sleep(2)
        self.driver.find_element_by_xpath("//div/span/div/label[2]/span/span[@class='el-radio__inner']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='请输入顾客称呼']").send_keys('gl郭京飞')
        self.driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']").send_keys('18707175056')
        self.driver.find_element_by_xpath(
            "//div[@class='btn-box']/div/div[2]/button/span[contains(text(),'订台')]").click()
        self.driver.find_element_by_xpath("//div[@class='pay-way-top-text' and contains(text(),'现金支付')]").click()
        self.driver.find_element_by_xpath("//div[@class='dialog-footer']/button[2]/span[text()='确 认']").click()
        self.driver.find_element_by_xpath(
            "//div[@style!='display: none;']/div/div[3]/div/button[2]/span[contains(text(),'收款成功')]").click()

    def reserve_deposit_table_sales(self):
        pass

    # 瓦 特1阿a有.弄啥嘞
    def reserve_free_table_customer(self):
        pass

    def reserve_free_table_sales(self):
        pass

    def cancel_reserve_table(self):
        self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'取消预定')]").click()
        self.driver.find_element_by_xpath("//textarea[@placeholder='请输入取消原因']").send_keys('邓邓取消')
        self.driver.find_element_by_xpath(
            "//div[@class='el-col el-col-12']/button[@type='button']/span[contains(text(),'确定')]").click()

    def cancel_reserve_button(self):
        # 验证取消按钮是否有效
        self.driver.find_element_by_xpath(
            "//div[@class='drawer']/div[5]/div/div/button/span[contains(text(),'取消')]").click()
        self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'订台')]").click()


# 进入各个模块
class IntoModule(object):
    def __init__(self, driver):
        self.driver = driver

    # 进入人事管理
    def into_personnel(self, management):
        if management == 'apartment':
            self.driver.find_element_by_xpath("//li[@role='menuitem']/span[contains(text(),'人事管理')]").click()
            self.driver.find_element_by_xpath("//div[@class='xi-header-flex']/div[contains(text(),'部门管理')]").click()
        else:
            self.driver.find_element_by_xpath("//li[@role='menuitem']/span[contains(text(),'人事管理')]").click()