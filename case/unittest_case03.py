from selenium import webdriver
import unittest
import time

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/IT/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.get("http://admin.wegui.cn/#/login")

user_name = '//*[@id="app"]/div/form/div[1]/div/div/input'
user_pwd = '/html/body/div/div/form/div[2]/div/div[1]/input'
button = '/html/body/div/div/form/div[3]/div/button'
login_fail = '/html/body/div[2]/div/h2'
driver.find_element_by_xpath(user_name).send_keys('xiaodwx1')
driver.find_element_by_xpath(user_pwd).send_keys('123456')
driver.find_element_by_xpath(button).click()
time.sleep(1)
a = driver.find_element_by_xpath(login_fail).text
print(a)
time.sleep(20)
driver.close()
