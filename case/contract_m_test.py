from selenium.webdriver.common.keys import Keys
from handle.get_utils import ActionUtil
from selenium import webdriver

mobileEmulation = {'deviceName': 'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
driver.get('http://wxadmin.wegui.cn/admin/#/')


