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
微信管理端审批
微信端发货申请&合同审批
'''

token = SessionToken()
driver = DriverInit().driver
rp = RegisterPage(driver)
def create_contract_approve(token):
    # 创建一个审批合同，xiaodwx申请及审批
    url_contracts = 'http://debug2.wegui.cn/v1/contracts'
    data_contracts = {"cabinetColor": "黑色", "images": [
        {"url": "http://debug2.wegui.cn/logistics/1597147928018_825093_1.jpg", "name": "1.jpg", "size": 2415133,
         "uid": 1597147928055, "status": "success"}],
            "siteName": "合同审批081201", "address": "在这里", "contact": "dxs", "phone": "188888888888", "sceneType": "观光景区",
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
    # 将审批申请放到待我审批
    url_agree_conrtract = 'http://debug2.wegui.cn/v1/contracts/' + res_get_oj.json()['objectId']
    data_agree_conrtract = {}
    res_agree_conrtract = requests.put(url_agree_conrtract, data=json.dumps(data_agree_conrtract), headers=token.web_headers())
    print(res_agree_conrtract)
    # 获取 待我审批 列表的第一个
    url_get_contracts_oj = 'http://debug2.wegui.cn/v1/approvalStages?limit=100&skip=0&order=-status,-createdAt&include=approval.originator.platform,approval.originator.agent,approval.originator.shop,approval.originator.site,approval.contract,approval.logistics&where=%7B%22status%22:%22pending%22,%22approval%22:%7B%22$inQuery%22:%7B%22where%22:%7B%22operator%22:%7B%22$inQuery%22:%7B%22where%22:%7B%22type%22:%7B%22$in%22:[%22platform%22,%22agent%22]%7D,%22objectId%22:%22lCYuzNNBmD%22%7D,%22className%22:%22_User%22%7D%7D,%22status%22:%7B%22$in%22:[%22pending%22,%22processing%22]%7D%7D,%22className%22:%22Approval%22%7D%7D,%22operator%22:%7B%22$inQuery%22:%7B%22where%22:%7B%22type%22:%7B%22$in%22:[%22platform%22,%22agent%22]%7D,%22objectId%22:%22lCYuzNNBmD%22%7D,%22className%22:%22_User%22%7D%7D%7D'
    res_get_contracts_oj = requests.get(url_get_contracts_oj, headers=token.web_headers())
    # 审批通过
    url_agree_approval = 'http://debug2.wegui.cn/v1/approvalStages/' + res_get_contracts_oj.json()[0]['objectId']
    data_agree_approval = {"remark":"auto","status":"done"}
    res = requests.put(url_agree_approval, data=json.dumps(data_agree_approval), headers=token.web_headers())
    return res.json()

def test_003(rp):
    driver.implicitly_wait(30)
    rp.open_url("http://admin.wegui.cn/#/login")
    driver.maximize_window()
    rp.web_login('xiaodwx', '123456')
    rp.open_web_menu('运营管理')
    rp.open_web_menu('合同审批（新）')
    time.sleep(5)
    rp.web_tab("已通过")
    time.sleep(5)
    rp.web_tab("查看")
    a = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='营业时间：']/following-sibling::*")))
    print(a.text)




if __name__ == '__main__':
    # create_contract_approve(token)
    test_003(rp)



