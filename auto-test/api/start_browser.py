# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


# =======根据电脑软件安装配置，请勿修改======
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/IT/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
# =======根据电脑软件安装配置，请勿修改======

driver.implicitly_wait(30)
driver.get("http://admin.wegui.cn/#/login")
# 判断页面是否有小铁寄存柜
EC.text_to_be_present_in_element_value('/html/body/div/div/form/h1', '小铁寄存柜')
# 页面查找指定元素是否存在，时间为30s
user = (By.XPATH, '/html/body/div/div/form/div[1]/div/div[1]/input')
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(user))
user_text = driver.find_element_by_xpath('/html/body/div/div/form/div[1]/div/div[1]/input')
user_text.send_keys('xiaodwx')
# 获取元素里的隐形文字
print(user_text.get_attribute('placeholder'))
# 获取元素里输入的值
print(user_text.get_attribute('value'))
driver.close()
