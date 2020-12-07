import requests
import json
from api.Base.runmethod import RunMethod
from ui.page.element_page import SessionToken


class KDGOrder:
    def __init__(self):
        self.rm = RunMethod()
        self.st = SessionToken()

    def find_site(self, site_name):
        find_site_url = 'https://lwd2.wegui.cn/v1/sites?limit=100&skip=0&include=shop.agent.superior.superior.superior.superior.superior.superior.superior.superior.superior&where={"name":{"$regex":"(?i)'+site_name+'"}}'
        find_site_res = self.rm.run_main('get', find_site_url, header=self.st.KDG_web_headers())
        site = find_site_res[0]['objectId']
        return site

    def find_cabinet(self, cab_no):
        find_cabinet_url = 'https://lwd2.wegui.cn/v1/cabinets?limit=100&skip=0&order=-createdAt&include=site,qrCode&where={"name":{"$regex":"(?i)'+cab_no+'"}}'
        find_cabinet_res = self.rm.run_main('get', find_cabinet_url, header=self.st.KDG_web_headers())
        cabinet = find_cabinet_res[0]['objectId']
        return cabinet

    def find_locker(self, cab_no):
        locker_list = []
        find_locker_url = 'https://lwd2.wegui.cn/v1/lockers?limit=360&skip=0&order=name&include=order.user,order.toUser&where={"cabinet":{"__type":"Pointer","className":"Cabinet","objectId":"'+self.find_cabinet(cab_no)+'"},"status":{"$ne":"disabled"}}'
        find_locker_res = self.rm.run_main('get', find_locker_url, header=self.st.KDG_web_headers())
        for i in range(0, len(find_locker_res)):
            locker = find_locker_res[i]['objectId']
            locker_list.append(locker)
            i += 1
        return locker_list

    def YT_occupy(self, cabinet_no, prohibit=None):
        cabinet_url = 'https://lwd2.wegui.cn/v1/cabinets/' + self.find_cabinet(cabinet_no)
        cabinet_res = self.rm.run_main('get', cabinet_url, header=self.st.KDG_web_headers())
        site_id = cabinet_res['site']['objectId']
        # 管理后台设置圆通占用的柜门类型
        url = 'https://lwd2.wegui.cn/v1/sites/' + site_id
        # {"prohibit":["s","m","l","xs"]}
        data = {"prohibit": list(prohibit)}
        self.rm.run_main('put', url, data=json.dumps(data), header=self.st.KDG_web_headers())

    # 管理后台-发送取件码
    def saas_send_code(self, order_id):
        send_code_url = 'https://lwd2.wegui.cn/v1/orders/' + str(order_id) + '/sendPickCode'
        send_code_data = {}
        order_res = self.rm.run_main('post', send_code_url, data=json.dumps(send_code_data), header=self.st.KDG_web_headers())
        return order_res['pick_code']

    # 管理后台-发送取件码
    def saas_send_no_code(self, order_id):
        send_code_url = 'https://lwd2.wegui.cn/v1/orders/' + str(order_id) + '/sendPickCode'
        send_code_data = {}
        order_res = self.rm.run_main('post', send_code_url, data=json.dumps(send_code_data), header=self.st.KDG_web_headers())
        return order_res

    # 管理后台-设置网点是否停用
    def saas_not_allow_arrears(self, site_name, arrears_status=True):
        arrears_url = 'https://lwd2.wegui.cn/v1/sites/' + KDGOrder.find_site(self, site_name)
        arrears_data = {"notAllowArrears": arrears_status}
        order_res = self.rm.run_main('put', arrears_url, data=json.dumps(arrears_data), header=self.st.KDG_web_headers())
        return order_res

    # 微信-重新发送取件码
    def KDG_send_code(self, order_id):
        send_code_url = 'https://lwd2.wegui.cn/v1/orders/' + str(order_id) + '/sendPickCode'
        send_code_data = {}
        order_res = self.rm.run_main('post', send_code_url, data=json.dumps(send_code_data), header=self.st.KDG_wx_headers())
        return order_res['pick_code']

    # 管理后台-修改手机号
    def saas_update_phone(self, order_id, phone):
        update_phone_url = 'https://lwd2.wegui.cn/v1/orders/' + order_id
        update_phone_data = {"phone": phone}
        order_res = self.rm.run_main('put', update_phone_url, data=json.dumps(update_phone_data), header=self.st.KDG_web_headers())
        return order_res

    # 微信-修改手机号
    def KDG_update_phone(self, order_id, phone):
        update_phone_url = 'https://lwd2.wegui.cn/v1/orders/' + order_id + '/phone'
        update_phone_data = {"phone": phone}
        order_res = self.rm.run_main('put', update_phone_url, data=json.dumps(update_phone_data), header=self.st.KDG_wx_headers())
        return order_res

    # 管理后台-关闭订单
    def saas_close_order(self, order_id=None, phone=None):
        if order_id:
            send_code_url = 'https://lwd2.wegui.cn/v1/orders/' + str(order_id) + '/close'
            send_code_data = {}
            order_res = self.rm.run_main('post', send_code_url, data=json.dumps(send_code_data), header=self.st.KDG_web_headers())
        else:
            phone_find_order_url = 'https://lwd2.wegui.cn/v1/orders?limit=100&skip=0&include=user,toUser,site,locker&order=-status,-createdAt&where={"type":"deliver","status":"processing","isCancel":false,"phone":"' + phone + '"}'
            phone_find_order_res = self.rm.run_main('get', phone_find_order_url, header=self.st.KDG_web_headers())
            phone_order_id = phone_find_order_res[0]['objectId']
            send_code_url = 'https://lwd2.wegui.cn/v1/orders/' + phone_order_id + '/close'
            send_code_data = {}
            order_res = self.rm.run_main('post', send_code_url, data=json.dumps(send_code_data), header=self.st.KDG_web_headers())
        return order_res['pick_code']

    # 管理后台-资金管理，获取目标商户账户余额
    def site_shop_account(self, site_shop_name):
        account_url = 'https://lwd2.wegui.cn/v1/accounts?limit=100&skip=0&order=-createdAt&include=agent,shop&where={"$or":[{"agent":{"$inQuery":{"where":{"name":{"$regex":"(?i)' + site_shop_name + '"}},"className":"Agent"}}},{"shop":{"$inQuery":{"where":{"name":{"$regex":"(?i)' + site_shop_name + '"}},"className":"Shop"}}}]}'
        account_res = self.rm.run_main('get', account_url, header=self.st.KDG_web_headers())
        return account_res[0]['voucher']

    # 快递柜下单
    def KDG_order(self, cab_no, locker_no, phone, deliveryNum, lockerType="s"):
        locker = self.find_locker(cab_no)[locker_no-1]
        # print(locker)
        order_url = 'https://lwd2.wegui.cn/v1/orders'
        order_data = {"cabinetId":self.find_cabinet(cab_no),"passwordEnable":False,"lockerType":lockerType,"lockerId":locker,"phone":phone,"deliveryNum":deliveryNum,"company":"快递公司"}
        order_res = self.rm.run_main('post', order_url, data=json.dumps(order_data), header=self.st.KDG_wx_headers())
        return order_res

    # 微信端结束订单打开柜门
    def KDG_close_order_open_door(self, order_id):
        order_url = 'https://lwd2.wegui.cn/v1/orders/' + order_id + '/unlock'
        order_data = {"closeOrder": True, "cancel": True, "cancelReason": "联系不上用户;AUTO"}
        order_res = self.rm.run_main('post', order_url, data=json.dumps(order_data), header=self.st.KDG_wx_headers())
        return order_res

    # 微信端结束订单不打开柜门
    def KDG_close_order_close_door(self, order_id):
        order_url = 'https://lwd2.wegui.cn/v1/orders/' + order_id + '/cancel'
        order_data = {"cancelReason":"联系不上用户;AUTO"}
        order_res = self.rm.run_main('post', order_url, data=json.dumps(order_data), header=self.st.KDG_wx_headers())
        return order_res