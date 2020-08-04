# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class LoginIn(unittest.TestCase):

    def setUp(self):
        # =======根据电脑软件安装配置，请勿修改======
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/IT/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        # =======根据电脑软件安装配置，请勿修改======

        self.driver.implicitly_wait(30)  # 等待30秒加载资源，30秒后无论加载是否完成都继续执行
        self.driver.get('http://admin.wegui.cn/#/login')
        user = self.driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div/input')
        user.send_keys("xiaodwx")
        pwd = self.driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div/input')
        pwd.send_keys("123456")
        button = self.driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button')
        button.click()

    def tearDown(self):
        self.driver.close()

    @unittest.skip('test_001')
    # 验证用户管理未关注搜索是否有效
    def test_001(self):
        manage = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/ul/div[2]/li/div')
        manage.click()
        user_manage = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/ul/div[2]/li/ul/div[1]/li')
        user_manage.click()
        search = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[1]/div[1]/div[1]/input')
        search.click()
        search_no_focus = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]')
        search_no_focus.click()
        selenium_text = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/span').text
        if selenium_text == '未关注':
            print('pass')
        else:
            print('fail')

    # 验证扣费规则搜索
    def test_002(self):
        manage = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/ul/div[3]/li/div')
        manage.click()
        deduction_rules = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/ul/div[3]/li/ul/div[10]/li')
        deduction_rules.click()
        search_site = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[1]/div[4]/span[4]')
        search_site.click()
        site_site = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[1]/span[2]/div/div/input')
        site_site.send_keys('az测试商户')
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li').click()
        time.sleep(5)
        selenium_text = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/div').text
        if selenium_text == 'az测试网2222':
            print('pass,已搜索出相应商户下的网点的扣费规则')
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div[2]/div[1]/button[1]').click()
            time.sleep(5)

            try:
                element = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/div')
                if element.text == 'az测试网2222':
                    print('pass')
                else:
                    print('fail')
            except Warning as e:
                print('fail', e)
        else:
            print('fail')


if __name__ == '__main__':
    unittest.main()
