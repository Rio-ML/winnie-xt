import json
import time

import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page.element_page import RegisterPage
from page.element_page import SessionToken
from util.DriverExchange import DriverInitExchange

'''
后台管理发货申请&合同审批
分成，主副柜，扣除费用对比
'''


token = SessionToken()
web_driver = DriverInitExchange().web_driver()
wx_driver = DriverInitExchange().wx_driver()
# rp = RegisterPage(driver)
contract_time = '2020-08-15'
contract_num = "合同审批081408"

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
    # expected_result = []
    platform_percent = res_get_oj.json()['shareRateMoney']['platform']
    shop_percent = res_get_oj.json()['shareRateMoney']['shop']
    other_percent = res_get_oj.json()['shareRateMoney']['other']
    percent = '平台：' + str(platform_percent) + '，商户：' + str(shop_percent) + '，' + str(other_percent)
    # expected_result.append(percent)
    cabinetCount = res_get_oj.json()['cabinetInfo'][0]['cabinetCount']
    sectionCount = res_get_oj.json()['cabinetInfo'][0]['sectionCount'] - cabinetCount
    lockerCount = res_get_oj.json()['cabinetInfo'][0]['lockerCount']
    cab_count = str(cabinetCount) + '主' + str(sectionCount) + '副' + str(lockerCount) + '门'
    # expected_result.append(cab_count)
    freightMoney = int(res_get_oj.json()['freightMoney']) / 100
    stickerMoney = int(res_get_oj.json()['stickerMoney']) / 100
    laborMoney = int(res_get_oj.json()['laborMoney']) / 100
    discount_money = '需扣除运费金额：' + str(freightMoney) + '，需扣除贴纸费用：' + str(stickerMoney) + '，需扣除人工费用：' + str(laborMoney)
    # expected_result.append(discount_money)
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
    # print(expected_result)
    # return expected_result


def web_contract_comparison():
    rp = RegisterPage(web_driver)
    web_test_result = []
    web_driver.implicitly_wait(30)
    rp.open_url("http://admin.wegui.cn/#/login")
    web_driver.maximize_window()
    rp.web_login('xd1645', 'abc123')
    rp.open_web_menu('运营管理')
    rp.open_web_menu('合同审批（新）')
    time.sleep(5)
    rp.web_tab("已通过")
    time.sleep(5)
    rp.web_tab("查看", contract_num)
    site_name = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='网点名称：']/following-sibling::*"))).text
    scene = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='场景分类：']/following-sibling::*"))).text
    scene_type = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='网点类型：']/following-sibling::*"))).text
    contact_name = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='联系人：']/following-sibling::*"))).text
    site_add = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='网点地址：']/following-sibling::*"))).text
    open_time = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='营业时间：']/following-sibling::*"))).text
    perday_money = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='每日营收：']/following-sibling::*"))).text
    open_daytime = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='营业时长：']/following-sibling::*"))).text
    place_people = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='场地人流量：']/following-sibling::*"))).text
    place_size = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='场地规模：']/following-sibling::*"))).text
    cor = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='合作模式：']/following-sibling::*"))).text
    # contract_type = WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.XPATH, "//div[text()='合同类型：']/following-sibling::*"))).text
    # contract_company = WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.XPATH, "//div[text()='签约公司：']/following-sibling::*"))).text
    payrule = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='支付规则：']/following-sibling::*"))).text
    percent = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='分成比例：']/following-sibling::*"))).text
    company_payrule = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='公司支付费用：']/following-sibling::*"))).text
    discount = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='需扣费用：']/following-sibling::*"))).text
    cab_enviroment = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='放柜环境：']/following-sibling::*"))).text
    other_enviroment = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='其他环境：']/following-sibling::*"))).text
    cab_color = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='柜组颜色：']/following-sibling::*"))).text
    cab_num = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='柜组总数：']/following-sibling::*"))).text
    associate = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='所需配件：']/following-sibling::*"))).text
    os = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='备注：']/following-sibling::*"))).text
    # 将结果批量加入list
    web_test_result.extend([site_name, scene, scene_type, contact_name, site_add, open_time, perday_money,
                        open_daytime, place_people, place_size, cor, payrule, percent,
                       company_payrule, discount, cab_enviroment, other_enviroment, cab_color, cab_num, associate, os])
    print(web_test_result)
    web_driver.close()
    return web_test_result


def wx_contract_comparison():
    rp = RegisterPage(wx_driver)
    wx_test_result = []
    wx_driver.implicitly_wait(30)
    # DriverInitExchange.wx_driver(wx_driver)
    rp.open_url("http://wxadmin.wegui.cn/admin/#/")
    # newwindow = 'window.open("http://wxadmin.wegui.cn/admin/#/")'
    # wx_driver.execute_script(newwindow)
    # wx_driver.switch_to_window(wx_driver.window_handles[1])
    rp.wx_login('xiaodwx', '123456')
    rp.open_xt_menu("合同审批(新)")
    WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='" + contract_num + "']"))).click()
    status = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='one done']/span"))).text
    apply_name = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='申请人']/following-sibling::*"))).text
    wx_cor = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='所属组织']/following-sibling::*"))).text
    apply_time = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='申请时间']/following-sibling::*"))).text
    cab_num = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='柜组数量']/following-sibling::*"))).text
    percent = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='分成比例']/following-sibling::*"))).text
    payrule = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='支付规则']/following-sibling::*"))).text
    site_name = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='网点名称']/following-sibling::*"))).text
    scene_type = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='场景分类']/following-sibling::*"))).text
    site_type = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='网点类型']/following-sibling::*"))).text
    add = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='详细地址']/following-sibling::*"))).text
    contact_name = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='联系人']/following-sibling::*"))).text
    contact_num = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='联系电话']/following-sibling::*"))).text
    os = WebDriverWait(wx_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='备注']/following-sibling::*"))).text
    wx_test_result.extend([status, apply_name, wx_cor, apply_time[0:10], cab_num, percent, payrule, site_name,
                            scene_type, site_type, add, contact_name, contact_num, os])
    wx_driver.close()
    print(wx_test_result)
    return wx_test_result


# bug:平台，合作商权限 保存后再添加编辑里面的数字会保存错误
def bug_001():
    rp = RegisterPage(web_driver)
    web_bug_test_result = []
    web_driver.implicitly_wait(30)
    rp.open_url("http://admin.wegui.cn/#/login")
    web_driver.maximize_window()
    # rp.web_login('xd1645', 'abc123')
    rp.web_login('xiaodwx', '123456')
    rp.open_web_menu('运营管理')
    rp.open_web_menu('合同审批（新）')
    rp.web_button("添加合同")
    # 移动到指定元素固定位置（指定元素在页面最下面）
    location_ele = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'柜组总数')]/parent::*/div/div/input")))
    ActionChains(web_driver).move_to_element(location_ele).perform()
    rp.web_input_text("收费规则", "1.5")
    rp.web_input_text("平台分成", "49.5")
    rp.web_input_text("商户分成", "20.5")
    rp.web_input_text("其它分成", "30")
    rp.web_input_text("公司支付费用", "1200.25")
    rp.web_button("需扣除运费-是")
    rp.web_input_text("需扣除运费", "10.11")
    rp.web_button("需扣除贴纸费用-是")
    rp.web_input_text("需扣除贴纸费用", "20.22")
    rp.web_button("人工费-是")
    rp.web_input_text("人工费", "30.33")
    web_driver.execute_script('document.documentElement.scrollTop=10000')
    rp.web_button("保存")
    rp.open_web_menu('合同审批（新）')
    rp.web_button("添加合同")
    rp.web_button("使用保存的合同申请")
    location_ele = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'柜组总数')]/parent::*/div/div/input")))
    ActionChains(web_driver).move_to_element(location_ele).perform()
    payrule = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'收费规则')]/parent::*/div/div/input"))).get_attribute('value')
    plat_percent = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'平台分成')]/parent::*/div/div/input"))).get_attribute('value')
    shop_percent = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'商户分成')]/parent::*/div/div/input"))).get_attribute('value')
    other_percent = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'其它分成')]/parent::*/div/div/input"))).get_attribute('value')
    com_payrule = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'公司支付费用')]/parent::*/div/div/input"))).get_attribute('value')
    freight = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'需扣除运费')]/parent::*/div/div/input"))).get_attribute('value')
    sticker = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'需扣除贴纸费用')]/parent::*/div/div/input"))).get_attribute('value')
    people_pay = WebDriverWait(web_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'人工费')]/parent::*/div/div/input"))).get_attribute('value')
    web_bug_test_result.extend([payrule, plat_percent, shop_percent, other_percent, other_percent, com_payrule, freight, sticker, people_pay])
    web_driver.close()
    print(web_bug_test_result)
    return web_bug_test_result


if __name__ == '__main__':
    # 创建一个合同审批并通过
    # create_contract_approve(token, contract_num)
    # selenium取出后台管理合同的值
    # web_result = web_contract_comparison()
    # 后台管理的预期结果
    # web_expect = [contract_num, '观光景区', '影视城', 'dxs/188888888888', '河北省秦皇岛市山海关区在这里', '00:02~07:12', '1', '2', '3', '4', '投放类', '5',
    #  '平台：50，商户：30，20', '100', '需扣除运费金额：10.11，需扣除贴纸费用：20.22，需扣除人工费用：30.33', '室外', '海边', '黑色', '1主3副32门',
    #  '定制贴纸（150/柜），定制雨棚（500/柜），脚杯，轮子', '这里是备注']
    # selenium取出微信管理端合同的值
    # wx_result = wx_contract_comparison()
    # wx_expect = ['已通过', 'xd1645', '测试自动化合同审批和发货申请', contract_time, '定制贴纸\n定制雨棚\n标准柜  1主3副', '平台：50\n商户：30\n其它：20', '5', contract_num, '观光景区', '影视城', '河北省秦皇岛市山海关区', 'dxs', '188888888888', '这里是备注']
    # 微信管理端的预期结果
    web_bug_result = bug_001()
    web_bug_expect = ['1.5', '49.5', '20.5', '30', '30', '1200.25', '10.11', '20.22', '30.33']
    print(web_bug_expect)
    if web_bug_result == web_bug_expect:
        print("通过")
    else:
        print("不通过")






