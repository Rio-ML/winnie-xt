# -*- coding:utf-8 -*-
# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
from case import common_operation
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from base.find_element import FindElement
from business.register_business import RegisterBusiness
from handle.register_handle import RegisterHandle

'''
PersonManage人事管理
test_001添加员工，不填的时候错误文案提示比对
test_002添加员工有必填项未填写，编辑其他员工时，错误提示不应该显示
test_003添加员工成功

'''


class PersonManage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://lzt.wegui.cn/#/login")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@placeholder='登陆账号']").send_keys('dxstest')
        self.driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys('dxs123123')
        self.driver.find_element_by_xpath("//button[@type='button']").click()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

    # @unittest.skip('不执行')
    # 添加员工，不填的时候错误文案提示比对
    def test_001(self):
        self.driver.implicitly_wait(30)
        common_operation.IntoModule.into_personnel(self, 'staff')
        self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'添加员工')]").click()
        self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'提交')]").click()
        result_1 = ec.text_to_be_present_in_element(
            (By.XPATH, "//input[@placeholder='请输入员工姓名']/parent::*/following-sibling::*"), '请输入姓名')(self.driver)
        print('请输入姓名', result_1)
        result_2 = ec.text_to_be_present_in_element(
            (By.XPATH, "//input[@placeholder='请输入手机号']/parent::*/following-sibling::*"), '请输入正确的电话号码！')(self.driver)
        print('请输入正确的电话号码！', result_2)
        result_3 = ec.text_to_be_present_in_element(
            (By.XPATH, "//input[@placeholder='请选择性别']/parent::*/parent::*/following-sibling::div[@class='el-form-item__error']"), '请选择性别')(self.driver)
        print('请选择性别', result_3)
        result_4 = ec.text_to_be_present_in_element(
            (By.XPATH, "//input[@placeholder='请输入民族']/parent::*/following-sibling::div[@class='el-form-item__error']"), '请输入民族')(self.driver)
        print('请输入民族', result_4)
        result_5 = ec.text_to_be_present_in_element(
            (By.XPATH, "//input[@placeholder='请选择出生日期']/parent::*/following-sibling::div[@class='el-form-item__error']"), '请选择出生日期')(self.driver)
        print('请选择出生日期', result_5)
        result_6 = ec.text_to_be_present_in_element(
            (By.XPATH, "//input[@placeholder='请输入身份证号']/parent::*/following-sibling::div[@class='el-form-item__error']"), '请输入正确的身份证号码')(self.driver)
        print('请输入正确的身份证号码', result_6)
        result_7 = ec.text_to_be_present_in_element(
            (By.XPATH, "//input[@placeholder='紧急联系人电话']/parent::*/following-sibling::div[@class='el-form-item__error']"), '请输入紧急联系人姓名')(self.driver)
        print('请输入紧急联系人姓名', result_7)
        result_8 = ec.text_to_be_present_in_element(
            (By.XPATH, "//input[@placeholder='请选择职位']/parent::*/parent::*/following-sibling::div[@class='el-form-item__error']"), '请输入职位')(self.driver)
        print('请输入职位', result_8)
        result_9 = ec.text_to_be_present_in_element(
            (By.XPATH, "//input[@placeholder='请选择']/parent::*/parent::*/following-sibling::div[@class='el-form-item__error']"), '请选择提成方式')(self.driver)
        print('请选择提成方式', result_9)

    # 添加员工有必填项未填写，编辑其他员工时，错误提示不应该显示
    def test_002(self):
        self.driver.implicitly_wait(30)
        common_operation.IntoModule.into_personnel(self, 'staff')
        self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'添加员工')]").click()
        self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'提交')]").click()
        self.driver.find_element_by_xpath("//i[@class='el-icon-arrow-left cursor' and contains(text(),'返回')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='cell' and contains(text(),'长江四号')]/parent::*/following-sibling::td[@class='el-table_1_column_12 is-center ']/div/button/span[contains(text(),'编辑')]").click()
        result_1 = ec.text_to_be_present_in_element(
            (By.XPATH, "//input[@placeholder='请输入员工姓名']/parent::*/following-sibling::*"), '请输入姓名')(self.driver)
        print('请输入姓名', result_1)
        if result_1:
            print("测试不通过")
        else:
            print("测试通过")

    # 添加员工成功
    def test_003(self):
        self.driver.implicitly_wait(30)
        common_operation.IntoModule.into_personnel(self, 'staff')
        self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'添加员工')]").click()
        self.driver.find_element_by_xpath("//input[@placeholder='请输入员工姓名']").send_keys("长江四号")
        self.driver.find_element_by_xpath("//input[@placeholder='请输入手机号']").send_keys("18622223333")
        self.driver.find_element_by_xpath("//input[@placeholder='请选择性别']").click()


if __name__ == '__main__':
    unittest.main()
