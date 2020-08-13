import time
from selenium import webdriver
from business.register_business import RegisterBusiness
from page.element_page import RegisterPage
from util.DriverInit import DriverInit
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import requests
import json
from page.element_page import RegisterPage
from page.element_page import SessionToken

'''
后台管理发货申请&合同审批
分成，主副柜，扣除费用对比
'''

token = SessionToken()
driver = DriverInit().driver
rp = RegisterPage(driver)
contract_num = "合同审批081315"
def create_contract_approve(token, contract_num):
    # 创建一个审批合同，xiaodwx申请及审批
    url_contracts = 'http://debug2.wegui.cn/v1/contracts'
    data_contracts = {"cabinetColor": "黑色", "images": [
        {"url": "http://debug2.wegui.cn/logistics/1597147928018_825093_1.jpg", "name": "1.jpg", "size": 2415133,
         "uid": 1597147928055, "status": "success"}],
            "siteName": contract_num, "address": "在这里", "contact": "dxs", "phone": "188888888888", "sceneType": "观光景区",
            "subSceneType": "影视城", "screen": "outDoor", "payRule": "5", "remark": "这里是备注",
            "shareRateMoney": {"platform": 50, "shop": 30, "other": "20"}, "factory": "",
            "checkRemark": {"check": "", "checking": "", "pending": "", "prepared": "", "suspend": "", "done": "",
                            "config": "", "canceled": "", "reject": "", "end": ""}, "cabinetInfo": [
            {"cabinetType": "balance", "name": "", "lockerCount": 32, "sectionCount": 4, "cabinetCount": 1, "locker": [0],
             "cabinetObj": {"wh": "750x450mm", "cabinet1": {"count": 1, "locker": 10},
                            "section1": {"count": 1, "locker": 12}, "section2": {"count": 1, "locker": 6},
                            "section3": {"count": 1, "locker": 4}}}],
            "paperEnable": True, "canopyEnable": True,
            "siteInfo": {"peopleCount": 3, "workTime": "2", "money": 1, "screenSize": 4, "otherMoney": 10000},
            "putType": "put", "areaCode": "130300", "openTime": 2, "closeTime": 432, "needFreight": True,
            "footCupEnable": True, "wheelEnable": True, "oceanEnable": True, "waterEnable": False, "signEnable": False,
            "freightMoney": 1011, "needSticker": True, "stickerMoney": 2022, "needLabor": True, "laborMoney": 3033,
            "payedRemark": "", "province": "河北省", "city": "秦皇岛市", "area": "山海关区",
            "originator": {"__type": "Pointer", "className": "_User", "objectId": "C0NqaTvfti"},
            "operators": ["lCYuzNNBmD"], "senders": []}
    res_get_oj = requests.post(url_contracts, data=json.dumps(data_contracts), headers=token.web_headers())
    expected_result = []
    platform_percent = res_get_oj.json()['shareRateMoney']['platform']
    shop_percent = res_get_oj.json()['shareRateMoney']['shop']
    other_percent = res_get_oj.json()['shareRateMoney']['other']
    percent = '平台：' + str(platform_percent) + '，商户：' + str(shop_percent) + '，' + str(other_percent)
    expected_result.append(percent)
    cabinetCount = res_get_oj.json()['cabinetInfo'][0]['cabinetCount']
    sectionCount = res_get_oj.json()['cabinetInfo'][0]['sectionCount'] - cabinetCount
    lockerCount = res_get_oj.json()['cabinetInfo'][0]['lockerCount']
    cab_count = str(cabinetCount) + '主' + str(sectionCount) + '副' + str(lockerCount) + '门'
    expected_result.append(cab_count)
    freightMoney = int(res_get_oj.json()['freightMoney']) / 100
    stickerMoney = int(res_get_oj.json()['stickerMoney']) / 100
    laborMoney = int(res_get_oj.json()['laborMoney']) / 100
    discount_money = '需扣除运费金额：' + str(freightMoney) + '，需扣除贴纸费用：' + str(stickerMoney) + '，需扣除人工费用：' + str(laborMoney)
    expected_result.append(discount_money)
    # 将审批申请放到待我审批
    url_agree_conrtract = 'http://debug2.wegui.cn/v1/contracts/' + res_get_oj.json()['objectId']
    data_agree_conrtract = {}
    requests.put(url_agree_conrtract, data=json.dumps(data_agree_conrtract), headers=token.web_headers())
    # 获取 待我审批 列表的第一个
    url_get_contracts_oj = 'http://debug2.wegui.cn/v1/approvalStages?limit=100&skip=0&order=-status,-createdAt&include=approval.originator.platform,approval.originator.agent,approval.originator.shop,approval.originator.site,approval.contract,approval.logistics&where=%7B%22status%22:%22pending%22,%22approval%22:%7B%22$inQuery%22:%7B%22where%22:%7B%22operator%22:%7B%22$inQuery%22:%7B%22where%22:%7B%22type%22:%7B%22$in%22:[%22platform%22,%22agent%22]%7D,%22objectId%22:%22lCYuzNNBmD%22%7D,%22className%22:%22_User%22%7D%7D,%22status%22:%7B%22$in%22:[%22pending%22,%22processing%22]%7D%7D,%22className%22:%22Approval%22%7D%7D,%22operator%22:%7B%22$inQuery%22:%7B%22where%22:%7B%22type%22:%7B%22$in%22:[%22platform%22,%22agent%22]%7D,%22objectId%22:%22lCYuzNNBmD%22%7D,%22className%22:%22_User%22%7D%7D%7D'
    res_get_contracts_oj = requests.get(url_get_contracts_oj, headers=token.web_headers())
    # 审批通过
    url_agree_approval = 'http://debug2.wegui.cn/v1/approvalStages/' + res_get_contracts_oj.json()[0]['objectId']
    data_agree_approval = {"remark":"auto","status":"done"}
    res = requests.put(url_agree_approval, data=json.dumps(data_agree_approval), headers=token.web_headers())
    print(res)
    print(expected_result)
    return expected_result


def test_003(rp):
    test_result = []
    driver.implicitly_wait(30)
    rp.open_url("http://admin.wegui.cn/#/login")
    driver.maximize_window()
    rp.web_login('xd1645', 'abc123')
    rp.open_web_menu('运营管理')
    rp.open_web_menu('合同审批（新）')
    time.sleep(5)
    rp.web_tab("已通过")
    time.sleep(5)
    rp.web_tab("查看", contract_num)
    percent = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='分成比例：']/following-sibling::*"))).text
    cab_num = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='柜组总数：']/following-sibling::*"))).text
    discount = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='需扣费用：']/following-sibling::*"))).text
    test_result.append(percent)
    test_result.append(cab_num)
    test_result.append(discount)
    print(test_result)
    driver.close()
    return test_result


if __name__ == '__main__':
    a = create_contract_approve(token, contract_num)
    b = test_003(rp)
    if a == b:
        print("通过")
    else:
        print("不通过")





