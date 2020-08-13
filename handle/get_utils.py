from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ActionUtil(object):
    def __init__(self, driver):
        self.driver = driver

    def input(self, xpath, value):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(value)

    def click(self, xpath):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()

    def clear(self, xpath):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath))).clear()

    def get_text(self, xpath):
        check_text = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return check_text.text

    def get_attribute(self, xpath, text):
        text_bool = WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))
        return text_bool
