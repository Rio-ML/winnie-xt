# -*- coding: utf-8 -*-

from selenium import webdriver


class DriverInitExchange:

    @staticmethod
    def wx_driver():
        # 设置成手机模式 开始
        mobile_emulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        # 设置成手机模式 结束

        # Windows 配置 开始
        driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        # Windows 配置 结束

        # mac 配置 开始
        # options.binary_location = "/Applications/IT/Google Chrome.app/Contents/MacOS/Google Chrome"
        # chrome_driver_binary = "/usr/local/bin/chromedriver"
        # driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        # mac 配置 结束
        return driver

    @staticmethod
    def web_driver():
        # mac 配置 开始
        # options = webdriver.ChromeOptions()
        # options.binary_location = "/Applications/IT/Google Chrome.app/Contents/MacOS/Google Chrome"
        # chrome_driver_binary = "/usr/local/bin/chromedriver"
        # driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        # mac 配置 结束

        # windows配置
        driver = webdriver.Chrome()
        # windows配置
        return driver
