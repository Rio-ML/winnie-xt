# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
from case import common_operation

'''
TestReserveTable桌台预订
TestOpenReserveTable预订开台
TestOpenTable开台
'''


class TestReserveTable(unittest.TestCase):

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
    # 顾客订台-仲夏夜之梦-有押金-现金-取消预订
    def test_001(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//div[@class='icon'][position()=1]").click()
        self.driver.find_element_by_xpath("//span[@class='el-radio-button__inner' and contains(text(),'散台666')]").click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//div[@class='xi-table-name' and contains(text(),'仲夏夜之梦')]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'订台')]").click()
            # 验证取消按钮是否有效
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='drawer']/div[5]/div/div/button/span[contains(text(),'取消')]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'订台')]").click()
            # 顾客订台
            time.sleep(2)
            self.driver.find_element_by_xpath("//div/span/div/label[2]/span/span[@class='el-radio__inner']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@placeholder='请输入顾客称呼']").send_keys('gl郭京飞')
            self.driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']").send_keys('18707175056')
            self.driver.find_element_by_xpath("//div[@class='btn-box']/div/div[2]/button/span[contains(text(),'订台')]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='pay-way-top-text' and contains(text(),'现金支付')]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='dialog-footer']/button[2]/span[text()='确 认']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@style!='display: none;']/div/div[3]/div/button[2]/span[contains(text(),'收款成功')]").click()
            # 判断是否订台成功
            time.sleep(2)
            customer_order = self.driver.find_element_by_xpath("//div[@class='drawer']/div/div/div[10]/span[@class='value']").text
            if customer_order == '自来客':
                print('pass')
                time.sleep(3)
                # 取消订台
                self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'取消预定')]").click()
                time.sleep(2)
                self.driver.find_element_by_xpath("//textarea[@placeholder='请输入取消原因']").send_keys('邓邓取消')
                time.sleep(2)
                self.driver.find_element_by_xpath("//div[@class='el-col el-col-12']/button[@type='button']/span[contains(text(),'确定')]").click()
                try:
                    time.sleep(2)
                    self.driver.find_element_by_xpath("//div[@class='dialog-content' and contains(text(),'取消原因：邓邓取消')]")
                    self.driver.find_element_by_xpath("//div[@class='el-dialog__body']/div[contains(text(),'房台名称：仲夏夜之梦')]")
                    self.driver.find_element_by_xpath("//div[@class='dialog-content' and contains(text(),'扣除押金：10.00')]")
                    print("显示正确")
                    self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'确认取消')]").click()
                except:
                    print("取消预订显示不一致")
            else:
                self.driver.save_screenshot("E:\\xt\\barselenium\\report\\customer_error.png")
        except Exception as e:
            print("有异常", e)

    # 业务员订台-瓦 特1阿a有.弄啥嘞-无押金-取消预订
    @unittest.skip('不执行')
    def test_002(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//div[@class='icon'][position()=1]").click()
        self.driver.find_element_by_xpath("//span[@class='el-radio-button__inner' and contains(text(),'散台666')]").click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//div[@class='xi-table-name' and contains(text(),'瓦 特1阿a有.弄啥嘞')]").click()
            self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'订台')]").click()
            self.driver.find_element_by_xpath("//input[@placeholder='请选择业务员']").send_keys('邓邓')
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='el-scrollbar']/div/ul/li[contains(text(),'邓邓')]").click()
            self.driver.find_element_by_xpath("//input[@placeholder='请输入顾客称呼']").send_keys('gl郭京飞')
            self.driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']").send_keys('18707175056')
            self.driver.find_element_by_xpath("//div[@class='btn-box']/div/div[2]/button/span[contains(text(),'订台')]").click()
            self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'确定')]").click()
            # 判断是否订台成功
            customer_order = self.driver.find_element_by_xpath("//div[@class='drawer']/div/div/div[10]/span[@class='value']").text
            if customer_order == '邓邓':
                print('pass')
                time.sleep(3)
                self.driver.find_element_by_xpath("//div[@class='el-col el-col-8']/button/span[contains(text(),'取消预定')]").click()
                self.driver.find_element_by_xpath("//textarea[@placeholder='请输入取消原因']").send_keys('邓邓取消')
                self.driver.find_element_by_xpath("//div[@class='el-col el-col-12']/button[@type='button']/span[contains(text(),'确定')]").click()
                try:
                    self.driver.find_element_by_xpath("//div[@class='dialog-content' and contains(text(),'取消原因：邓邓取消')]")
                    self.driver.find_element_by_xpath("//div[@class='el-dialog__body']/div[contains(text(),'房台名称：瓦 特1阿a有.弄啥嘞')]")
                    self.driver.find_element_by_xpath("//div[@class='dialog-content' and contains(text(),'扣除押金：0.00')]")
                    print("显示正确")
                    self.driver.find_element_by_xpath("//button[@type='button']/span[contains(text(),'确认取消')]").click()
                except:
                    print("取消预订显示不一致")

            else:
                self.driver.save_screenshot("E:\\xt\\barselenium\\report\\sales_error.png")

        except Exception as e:
            print("有异常", e)


class TestOpenReserveTable(unittest.TestCase):

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

    def test_001(self):
        pass


class TestOpenTable(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
