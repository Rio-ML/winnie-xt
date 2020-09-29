from selenium.webdriver.common.keys import Keys
from handle.get_utils import ActionUtil
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

'''手机就浏览器'''
mobileEmulation = {'deviceName': 'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
driver.get('http://wxadmin.cn/admin/#/')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='用户名']"))).send_keys('username')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='密码']"))).send_keys('password')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='mint-button']"))).click()
driver.close()

'''网页版'''
driver = webdriver.Chrome()
driver.get('http://wxadmin.cn/admin/#/')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='用户名']"))).send_keys('username')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='密码']"))).send_keys('password')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='mint-button']"))).click()
driver.close()
