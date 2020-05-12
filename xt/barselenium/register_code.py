# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import random



# =======根据电脑软件安装配置，请勿修改======
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/IT/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
# =======根据电脑软件安装配置，请勿修改======chrome_driver_binary, chrome_options=options)


# 浏览器初始化
def driver_init():
    driver.get("http://admin.wegui.cn/#/login")
    time.sleep(60)


# 获取element信息
def get_element(id):
    element = driver.find_element_by_xpath(id)
    return element


# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('123456789abcdefghijk', 8))
    return user_info


# 运行主程序
def run_main():
    user_name = 'xiaodwx'
    user_pwd = '123456'
    driver_init()
    get_element('/html/body/div/div/form/div[1]/div/div[1]/input').send_keys(user_name)
    get_element('/html/body/div/div/form/div[2]/div/div[1]/input').send_keys(user_pwd)
    get_element('/html/body/div/div/form/div[3]/div/button').click()
    driver.close()

