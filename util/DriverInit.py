# -*- coding: utf-8 -*-

from selenium import webdriver


class DriverInit:
    def __init__(self):
        # 设置成手机模式 开始
        # mobile_emulation = {'deviceName': 'iPhone X'}
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('mobileEmulation', mobile_emulation)
        # 设置成手机模式 结束
        # Windows 配置 开始
        # self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        # Windows 配置 结束
        # mac 配置 开始
        # options.binary_location = "/Applications/IT/Google Chrome.app/Contents/MacOS/Google Chrome"
        # chrome_driver_binary = "/usr/local/bin/chromedriver"
        # self.driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        # mac 配置 结束

        # Windows设置成网页模式 开始
        self.driver = webdriver.Chrome()
        # Windows设置成网页模式 结束
