from selenium.webdriver.common.keys import Keys
from ui.handle.get_utils import ActionUtil
from selenium import webdriver
import requests
import json

url = 'https://lwd2.wegui.cn/v1/login'
headers1 = {"Content-Type": "application/json", "Xi-App-Id": "ce5cec2cfd1440759db6fa992b0641b7"}
data1 = {"username": "dxsauto", "password": "abc123"}
res = requests.post(url, data=json.dumps(data1), headers=headers1)
session = res.json()['sessionToken']
url = 'https://lwd2.wegui.cn/v1/sites/xN3ZvEoioM'
headers2 = {"Content-Type": "application/json", "Xi-App-Id": "ce5cec2cfd1440759db6fa992b0641b7",
           "Xi-Session-Token": session}
# data = {"prohibit":["s","m","l","xs"]}
data2 = {"prohibit": ["s"]}
requests.put(url, data=json.dumps(data2), headers=headers2)
