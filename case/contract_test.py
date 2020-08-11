# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from business.register_business import RegisterBusiness
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unittest
import time

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



