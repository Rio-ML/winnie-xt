# -*- coding: utf-8 -*-
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
import os
import sys



class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始')

    @classmethod
    def tearDownClass(cls):
        print('结束')

    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.binary_location = "/Applications/IT/Google Chrome.app/Contents/MacOS/Google Chrome"
        # chrome_driver_binary = "/usr/local/bin/chromedriver"
        # self.driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        self.driver.get("http://admin.wegui.cn/#/login")
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(__file__)) + '/report/' + case_name + '.png'
                self.driver.save_screenshot(file_path)
        self.driver.close()


    # @unittest.skip('不执行')
    def test_01_login_user_error(self):
        user_name_error = self.login.login_user_name_error('', '123456')
        self.assertTrue(user_name_error, '有 bug 呀')
        # if user_name_error == True:
        #     print("登录不成功，此条case执行成功")
        # else:
        #     print("有 bug 呀")

    def test_02_login_pwd_error(self):
        user_pwd_error = self.login.login_user_pwd_error('xiaodwx', '')
        self.assertTrue(user_pwd_error, '有 bug 呀')
        # if user_pwd_error == True:
        #     print("登录不成功，此条case执行成功")
        # else:
        #     print("有 bug 呀")

    def test_03_login_success(self):
        user_success = self.login.user_base('xiaodwx', '123456')
        self.assertTrue(user_success, '有 bug 呀')
        # if self.login.register_success() == True:
        #     print("登录成功")
        # else:
        #     print('登录失败')

    def test_04_login_fail(self):
        user_fail = self.login.login_fail('xiaodwx1', '123456')
        self.assertFalse(user_fail, '有 bug 呀')

    def test_05_login_fail(self):
        user_fail = self.login.login_fail('xiaodwx1', '123456')
        self.assertFalse(user_fail, '有 bug 呀')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_04_login_fail'))
    unittest.TextTestRunner().run(suite)
