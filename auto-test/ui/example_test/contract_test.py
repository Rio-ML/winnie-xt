# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from ui.business.register_business import RegisterBusiness
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unittest
import time
# commit
mobileEmulation = {'deviceName': 'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

driver.get('http://wxadmin.wegui.cn/admin/#/')

def Input(driver, xpath, value):
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(value)


def Click(driver, xpath):
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()


def Get_text(driver, xpath):
    check_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath))).text()
    return check_text


def Get_attribute(driver, xpath, text):
    text_bool = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))
    return text_bool


def add_photo(driver, xpath, photo):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys(photo)


Input(driver, "//input[@placeholder='用户名']", 'xiaod90')
Input(driver, "//input[@placeholder='密码']", '123456')
Click(driver, "//button[@class='mint-button primary-btn mint-button--default mint-button--large']")
Click(driver, "//div[contains(text(),'合同审批(新)')]/parent::*/parent::*")
Click(driver, "//span[contains(text(),'添加申请')]")
if Get_attribute(driver, "//div[@class='edit-cabinet']/div[@class='title']", "请仔细填写合同审批"):
    print("开始填写合同审批")
    Input(driver, "//input[@placeholder='请输入网点名称']", "2020061601")
    # Click(driver, "//label[text()='需扣除运费']")
    # driver.find_element_by_css_selector("[for='needFreight']").send_keys(Keys.ENTER)

    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='需扣除运费']/preceding-sibling::*"))).click()
    # 滚动到最底部
    # js = "var q=document.documentElement.scrollTop=100000"
    # driver.execute_script(js)
    # time.sleep(3)
    # add_photo(driver, "//input[@type='file']", "E:/xt/xtselenium/util/v.png")
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys("E:/xt/xtselenium/util/v.png")
    # file = driver.find_element_by_xpath("//input[@type='file']")
    # file.send_keys("E:/xt/xtselenium/util/v.png")
else:
    print("合同审批文案对比失败")

