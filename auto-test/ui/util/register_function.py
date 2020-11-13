# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import random
from ui.base.find_element import FindElement


# # =======根据电脑软件安装配置，请勿修改======
# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/IT/Google Chrome.app/Contents/MacOS/Google Chrome"
# chrome_driver_binary = "/usr/local/bin/chromedriver"
# driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
# # =======根据电脑软件安装配置，请勿修改======
# driver.get("http://admin.wegui.cn/#/login")


class RegisterFunction(object):
    def __init__(self, url):
        self.driver = self.get_driver(url)

    def get_driver(self, url):
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/IT/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = "/usr/local/bin/chromedriver"
        driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        driver.get(url)
        return driver

    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

     # 获取元素
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890qwertyuio', 6))
        return user_info

    def main(self):
        user_name_info = 'xiaodwx'
        user_pwd = '123456'
        self.send_user_info('user_name', user_name_info)
        self.send_user_info('user_pwd', user_pwd)
        self.get_user_element('register_confirm_button').click()
        code_error = self.get_user_element('')
        if code_error == None:
            print('登录成功')
        else:
            self.driver.save_screenshot("/Users/ranmenglong/workspace/winnie/xtselenium/config/login_error.png")
        time.sleep(10)
        self.driver.close()


if __name__ == '__main__':
    register_function = RegisterFunction('http://admin.wegui.cn/#/login')
    register_function.main()
