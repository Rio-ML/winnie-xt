# import unittest
# import os
import re  # 用于正则
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
from selenium import webdriver  # 用于打开网站
import time  # 代码运行停顿
import cv2
import numpy as np
import os
from io import BytesIO
from selenium import webdriver
import unittest
import time
from ui.business.register_business import RegisterBusiness
from ui.page.element_page import RegisterPage
from ui.util.DriverInit import DriverInit
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import requests
import json
# class RunCase(unittest.TestCase):
#     def test_case01(self):
#         # case_path = os.path.join(os.getcwd(), 'case')    # windows可以使用，mac报错
#         case_path = os.path.abspath(os.path.dirname(__file__))  # 要获取当前文件所在文件夹的目录，才能让TestLoader扫描当前目录下的文件
#         print(case_path)
#         suite = unittest.defaultTestLoader.discover(case_path, 'unittest_*.py')
#         unittest.TextTestRunner().run(suite)
#
#
# if __name__ == '__main__':
#     unittest.main()
from pytesseract.pytesseract import image_to_string
# from PIL import Image
# import pytesseract
# image = Image.open(r'E:\xt\image\test2.jpg')#打开图片
# result = pytesseract.image_to_string(image, lang='chi_sim')#使用简体中文字库识别图片并返回结果
# print(result)



# class VerificationCode:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.find_element = self.driver.find_element_by_xpath
#
#     def get_pictures(self):
#         self.driver.get('http://admin.wegui.cn/#/login')  # 打开登陆页面
#         self.driver.save_screenshot('pictures.png')  # 全屏截图
#         page_snap_obj = Image.open('pictures.png')
#         img = self.find_element("//span[@id='code']")  # 验证码元素位置
#         time.sleep(1)
#         location = img.location
#         size = img.size  # 获取验证码的大小参数
#         left = location['x']
#         top = location['y']
#         right = left + size['width']
#         bottom = top + size['height']
#         image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
#         image_obj.show()  # 打开切割后的完整验证码
#         self.driver.close()  # 处理完验证码后关闭浏览器
#         return image_obj
#
#     def processing_image(self):
#         image_obj = self.get_pictures()  # 获取验证码
#         img = image_obj.convert("L")  # 转灰度
#         pixdata = img.load()
#         w, h = img.size
#         threshold = 160
#         # 遍历所有像素，大于阈值的为黑色
#         for y in range(h):
#             for x in range(w):
#                 if pixdata[x, y] < threshold:
#                     pixdata[x, y] = 0
#                 else:
#                     pixdata[x, y] = 255
#         return img
#
#     def delete_spot(self):
#         images = self.processing_image()
#         data = images.getdata()
#         w, h = images.size
#         black_point = 0
#         for x in range(1, w - 1):
#             for y in range(1, h - 1):
#                 mid_pixel = data[w * y + x]  # 中央像素点像素值
#                 if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
#                     top_pixel = data[w * (y - 1) + x]
#                     left_pixel = data[w * y + (x - 1)]
#                     down_pixel = data[w * (y + 1) + x]
#                     right_pixel = data[w * y + (x + 1)]
#                     # 判断上下左右的黑色像素点总个数
#                     if top_pixel < 10:
#                         black_point += 1
#                     if left_pixel < 10:
#                         black_point += 1
#                     if down_pixel < 10:
#                         black_point += 1
#                     if right_pixel < 10:
#                         black_point += 1
#                     if black_point < 1:
#                         images.putpixel((x, y), 255)
#                     black_point = 0
#         # images.show()
#         return images
#
#     def image_str(self):
#         image = self.delete_spot()
#         pytesseract.pytesseract.tesseract_cmd = r"D:\DXS\package\OCR\tesseract.exe"  # 设置pyteseract路径
#         result = pytesseract.image_to_string(image)  # 图片转文字
#         resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
#         result_four = resultj[0:4]  # 只获取前4个字符
#         # print(resultj)  # 打印识别的验证码
#         return result_four
#
#
# if __name__ == '__main__':
#     a = VerificationCode()






# driver = webdriver.Chrome()
# driver.get('http://admin.wegui.cn/#/login')  # 打开登陆页面
# driver.save_screenshot('pictures.png')  # 全屏截图
# page_snap_obj = Image.open('pictures.png')
# img = driver.find_element_by_xpath("//span[@id='code']")  # 验证码元素位置
# time.sleep(3)
# location = img.location
# size = img.size  # 获取验证码的大小参数
# left = location['x']
# top = location['y']
# right = left + size['width']
# bottom = top + size['height']
# image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
# # image_obj.show()  # 打开切割后的完整验证码
# driver.close()  # 处理完验证码后关闭浏览器
#
# img = image_obj.convert("L")  # 转灰度
# pixdata = img.load()
# w, h = img.size
# threshold = 145  # 该阈值不适合所有验证码，具体阈值请根据验证码情况设置
# # 遍历所有像素，大于阈值的为黑色
# for y in range(h):
#     for x in range(w):
#         if pixdata[x, y] < threshold:
#             pixdata[x, y] = 0
#         else:
#             pixdata[x, y] = 255
# img.save('E:/xt/image/test2.jpg')


# # 黑白反转
# #读取彩色原图
# src = cv2.imread('E:/xt/image/test2.jpg', 1)
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# img_info = src.shape
# image_height = img_info[0]
# image_weight = img_info[1]
# dst = np.zeros((image_height, image_weight, 1), np.uint8)
# for i in range(image_height):
#     for j in range(image_weight):
#         grayPixel = gray[i][j]
#         dst[i][j] = 255-grayPixel
# cv2.imshow('gary', dst)
# cv2.waitKey(0)
# # img_info.show()


# pytesseract.pytesseract.tesseract_cmd = r"D:\DXS\package\OCR\tesseract.exe"  # 设置pyteseract路径
# result = pytesseract.image_to_string('E:/xt/image/test2.jpg')  # 图片转文字
# resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
# result_four = resultj[0:3]  # 只获取前4个字符
# print(resultj)  # 打印识别的验证码
# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
# list2 = list1.copy()
# list2.remove("Runoob")
# print("list1 列表: ", list1)
# print("list2 列表: ", list2)
# url = 'http://debug2.wegui.cn/v1/users/hYerDH4nHm'
# headers = {"Content-Type": "application/json",
#            "Xi-App-Id": "0a8020002101b2ddc7626fca179adf70",
#            "Xi-Session-Token": "r:c8b10a1783009230e01f3783e2441898"}
# data = {"username":"shop","roleType":"main","gender":"male","phone":"asd","remark":"","nickname":"sad","status":"normal","passport":{"web":True,"wxadmin":True,"withdraw":True,"quickManage":True,"orderNRecord":True,"baseCount":True},"managerRole":{"__type":"Pointer","className":"ManagerRole","objectId":"vlPSXU5EM3"}}
# put = requests.put(url, data=json.dumps(data), headers=headers)
# print(put.json())
# print("权限错误", '\n', 'right_list', '\n', 'lists')
# role = 'regulator'
# data = '{"username":"shop","roleType":"operator","gender":"male","phone":"asd","remark":"","nickname":"sad","status":"normal",' \
#        '"passport":{"web":true,"wxadmin":true,"withdraw":true,"quickManage":true,"orderNRecord":true,"baseCount":true},' \
#        '"managerRole":{"__type":"Pointer","className":"ManagerRole","objectId":"tKTfO0KLu5"}}'
# list = {'main': 'vlPSXU5EM3', 'operator': 'G6manc1tnY', 'accountant': 'tKTfO0KLu5', 'partner': 'phmyTlJNle', 'regulator': 'AtfQDan6NH'}
# data_obj = json.loads(data)
# data_obj['roleType'] = role
# data_obj['managerRole']['objectId'] = list[role]
# print(list[role])
# print(json.dumps(data_obj))

# a =  '2020-08-14 14:21:56'
# print(a[0:10])
# a = ['1.5', '49.5', '20.5', '30', '30', '1200.25', '10.11', '20.22', '30.33']
# b = ['1.5', '49.5', '20.5', '30', '30', '1200.25', '10.11', '20.22', '30.33']
# if a == b:
#     print("通过")
# else:
#     print("不通过")
# contract_num = "合同审批081408"
# headers = {"Content-Type": "application/json",
#            "Xi-App-Id": "0a8020002101b2ddc7626fca179adf70",
#            "Xi-Session-Token": "r:fc3eafc70e0cb4c8ab6752f47e92f9b0"}
# url_contracts = 'http://debug2.wegui.cn/v1/contracts'
# data_contracts = {"cabinetColor": "黑色", "images": [
#     {"url": "http://debug2.wegui.cn/logistics/1597147928018_825093_1.jpg", "name": "1.jpg", "size": 2415133,
#      "uid": 1597147928055, "status": "success"}],
#                   "siteName": contract_num, "address": "在这里", "contact": "dxs", "phone": "188888888888",
#                   "sceneType": "观光景区",
#                   "subSceneType": "影视城", "screen": "outDoor", "payRule": "5", "remark": "这里是备注",
#                   "shareRateMoney": {"platform": 50, "shop": 30, "other": "20"}, "factory": "",
#                   "checkRemark": {"check": "", "checking": "", "pending": "", "prepared": "", "suspend": "", "done": "",
#                                   "config": "", "canceled": "", "reject": "", "end": ""}, "cabinetInfo": [
#         {"cabinetType": "balance", "name": "", "lockerCount": 32, "sectionCount": 4, "cabinetCount": 1, "locker": [0],
#          "cabinetObj": {"wh": "750x450mm", "cabinet1": {"count": 1, "locker": 10},
#                         "section1": {"count": 1, "locker": 12}, "section2": {"count": 1, "locker": 6},
#                         "section3": {"count": 1, "locker": 4}}}],
#                   "paperEnable": True, "canopyEnable": True,
#                   "siteInfo": {"peopleCount": 3, "workTime": "2", "money": 1, "screenSize": 4, "otherMoney": 10000},
#                   "putType": "put", "areaCode": "130300", "openTime": 2, "closeTime": 432, "needFreight": True,
#                   "footCupEnable": True, "wheelEnable": True, "oceanEnable": True, "waterEnable": False,
#                   "signEnable": False,
#                   "freightMoney": 1011, "needSticker": True, "stickerMoney": 2022, "needLabor": True,
#                   "laborMoney": 3033,
#                   "payedRemark": "", "province": "河北省", "city": "秦皇岛市", "area": "山海关区",
#                   "originator": {"__type": "Pointer", "className": "_User", "objectId": "C0NqaTvfti"},
#                   "operators": ["lCYuzNNBmD"], "senders": ["RR9yjT56Ry"]}
# res_get_oj = requests.post(url_contracts, data=json.dumps(data_contracts), headers=headers)
# print(res_get_oj)

# 微信端关闭订单
# orderid = []
# headers = {"Content-Type": "application/json",
#            "Xi-App-Id": "0a8020002101b2ddc7626fca179adf70",
#            "Xi-Session-Token": "r:f8d18ca92435f20a4649353513052971"}
# url_order = 'https://azapi.wegui.cn/v1/orders?skip=0&limit=100&order=-startAt&include=user,coupon&where=%7B%22status%22:%22processing%22%7D'
# get_orderid = requests.get(url_order, headers=headers)
#
# try:
#     for i in range(0, 73):
#         a = get_orderid.json()[i]['objectId']
#         i += 1
#         orderid.append(a)
#     print(orderid)
# except IndexError as e:
#     print(e)
#
# for order in orderid:
#     url = "https://azapi.wegui.cn/v1/orders/" + order + "/unlock"
#     data_contracts = {"closeOrder": True}
#     headers = {"Content-Type": "application/json",
#                "Xi-App-Id": "0a8020002101b2ddc7626fca179adf70",
#                "Xi-Session-Token": "r:f8d18ca92435f20a4649353513052971"}
#     res_get_oj = requests.post(url, data=json.dumps(data_contracts), headers=headers)
#     print(res_get_oj.json())

# 后台管理获取所有锁id
# orderid = []
# url = "http://debug2.wegui.cn/v1/lockers?limit=360&skip=0&order=name&include=order.user,cabinet&where=%7B%22cabinet%22:%7B%22__type%22:%22Pointer%22,%22className%22:%22Cabinet%22,%22objectId%22:%22AKpPpQektg%22%7D,%22status%22:%7B%22$ne%22:%22disabled%22%7D%7D"
# headers = {"Content-Type": "application/json",
#            "Xi-App-Id": "0a8020002101b2ddc7626fca179adf70",
#            "Xi-Session-Token": "r:61bb0b1fe26963909c4f5aaf74e2e8ee"}
# get_orderid = requests.get(url, headers=headers)
# try:
#     for i in range(0, 72):
#         a = get_orderid.json()[i]['objectId']
#         print(a)
#         i += 1
#         orderid.append(a)
#     print(orderid)
# except IndexError as e:
#     print(e)
# list = ['tt', 'aa', 'bb']
# if 'ee' in list:
#     list.remove('ee')
#     print(list)
# else:
#     # list.remove('ee')
#     print(list)

# value = '18707175056'
# a = list(value)
# print(a)
# for i in a:
#     # self.d(resourceId=class_map[i]).click()
#     print(i)
# from api.Base.runmethod import RunMethod
# from api.data import data_config
#
#
# order_url = 'https://azapi.wegui.cn/v1/orders'
# # order_data = {"cabinetId": self.find_cabinet(cab_no), "rentType": "short", "lockerType": "s",
# #               "passwordEnable": False, "prepaid": 1, "manualLockerEnable": True, "lockerId": "zxdG04YqEi"}
# order_data = {"cabinetId": "AKpPpQektg", "rentType": "short", "lockerType": "s",
#               "passwordEnable": False, "prepaid": 0, "manualLockerEnable": True, "lockerId": "zxdG04YqEi"}
# order_res = RunMethod().run_main('post', order_url, data=json.dumps(order_data), header=data_config.wx_headers())
# print(order_res)
# from itertools import combinations, permutations
# list1=list(permutations([1,1,1,2,2,2],6))
# list2={}.fromkeys(list1).keys()
# print(list2)

# # 小明有两种读书方式，精读1本或者速读2本，现在他告诉你他读了N本书，那么他有多少种读书方式呢？
# from scipy.special import comb
# def ou_num(n):
#     list1 = []
#     list2 = []
#     x = -2
#     for i in range(1, int(n/2+1)+1):
#         list1.append(n)
#         n -= 2
#         x += 2
#         list2.append(x)
#     return list1, list2
#
# def ji_num(n):
#     list1 = []
#     list2 = []
#     x = 0
#     for i in range(1, int(n/2+1)+1):
#         list1.append(n)
#         n -= 2
#         list2.append(x)
#         x += 2
#     return list1, list2
#
# def all_num(n):
#     if n % 2 == 0:
#         a = ou_num(n)[0]
#         b = ou_num(n)[1]
#         list_cum_result = []
#         for i in range(1, len(a)):
#             way = int(comb(a[i] + b[i] / 2, a[i]))
#             list_cum_result.append(way)
#         return sum(list_cum_result, 1)
#     else:
#         a = ji_num(n)[0]
#         b = ji_num(n)[1]
#         list_cum_result = []
#         for i in range(1, len(a)):
#             way = int(comb(a[i] + b[i] / 2, a[i]))
#             list_cum_result.append(way)
#         return sum(list_cum_result, 1)
#
# if __name__ == '__main__':
#     a = input("Enter a number: ")
#     print('小明的读书方式总数：', all_num(int(a)))


# 输入十六进制，输出十进制
# print(hex(16))

# 给一个数组，将数组内的偶数放后面，奇数放前面
# a_list = [5,8,7,6,1,2,9]
# a_list = [1,28,5,6,7,30,9]
# ji_list = []
# ou_list = []
# for i in a_list:
#     if i % 2 == 0:
#         ou_list.append(i)
#     else:
#         ji_list.append(i)
# print(ji_list+ou_list)
a = 'abcd'
print(int(a))

