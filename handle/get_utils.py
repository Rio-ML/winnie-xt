from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Action_util(object):
    def __init__(self, driver):
        self.driver = driver

    def Input(driver, xpath, value):
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(value)

    def Click(driver, xpath):
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()

    def Clear(driver, xpath):
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath))).clear()

    def Get_text(driver, xpath):
        check_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath))).text()
        return check_text

    def Get_attribute(driver, xpath, text):
        text_bool = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))
        return text_bool
