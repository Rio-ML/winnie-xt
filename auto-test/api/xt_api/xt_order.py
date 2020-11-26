import requests
import json
from api.Base.runmethod import RunMethod
from api.data import data_config as dc


class XTOrder:
    def __init__(self):
        self.rm = RunMethod()

    def find_user(self, user_name):
        user_list = []
        find_user_url = 'http://debug2.wegui.cn/v1/users?limit=100&skip=0&order=-createdAt&include=wallet,fromSite,weixin&where={"type":"consumer","nickname":"' + user_name + '"}'
        find_user_res = self.rm.run_main('get', find_user_url, header=dc.pc_headers('xiaodwx'))
        for i in range(0, len(find_user_res)):
            user = find_user_res[i]['objectId']
            user_list.append(user)
            i += 1
        return user_list

    def find_cabinet(self, cab_no):
        find_cabinet_url = 'http://debug2.wegui.cn/v1/cabinets?limit=100&skip=0&order=-createdAt&include=site.shop,qrCode.weixin,slave,cabinetConfig&where={"$or":[{"name":{"$regex":"(?i)z011905751622"}},{"mac":{"$regex":"(?i)'+cab_no+'"}}]}'
        find_cabinet_res = self.rm.run_main('get', find_cabinet_url, header=dc.pc_headers('xiaodwx'))
        cabinet = find_cabinet_res[0]['objectId']
        return cabinet

    # 重置手机号 winnie = YEhBS9rJab
    def reset_phone(self, user_name_id):
        for i in self.find_user(user_name_id):
            reset_url = 'http://debug2.wegui.cn/v1/users/' + i
            reset_data = {"phone": "", "delFace": False}
            self.rm.run_main('put', reset_url, data=json.dumps(reset_data), header=dc.pc_headers('xiaodwx'))

    # 默认配置收费规则 按时+不支持密码存包强制输入手机号+长/短租
    # passwordEnable是否支持密码存包（True支持，False不支持）
    # passwordEnable为True时，forcePhoneEnable应该为False
    # passwordEnable为True时，birthdayEnable，idCardEnable为True分别对应开启生日日期存包和身份证存包
    # passwordEnable为False时,forcePhoneEnable为True是强制输入手机号，False是不用输入手机号
    # countRentEnable，longRentEnable，shortRentEnable为True时对应开启按柜，长租，短租
    def set_pay_rule(self, cab_no, passwordEnable=False, longRentEnable=False, shortRentEnable=True, countRentEnable=False, type='b',birthdayEnable=False,idCardEnable=False,forcePhoneEnable=True):
        set_pay_rule_url = 'http://debug2.wegui.cn/v1/cabinets/' + self.find_cabinet(cab_no) + '/payRule'
        set_pay_rule_data = {"forgetPayRule":{"s":{"prepaid":0},"m":{"prepaid":0},"l":{"prepaid":0}},"longPayRule":{"s":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":1440,"perMoney":1,"perTime":14400,"prepaid":1,"topMoney":0,"topTime":0,"unlockCount":0},"m":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":1440,"perMoney":1,"perTime":14,"prepaid":1,"topMoney":0,"topTime":0,"unlockCount":0},"l":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":1440,"perMoney":1,"perTime":14,"prepaid":1,"topMoney":0,"topTime":0,"unlockCount":0}},"payRule":{"s":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":0,"perMoney":1,"perTime":2,"prepaid":1,"topMoney":0,"topTime":0,"unlockCount":6,"endTime":1391},"m":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":0,"perMoney":1,"perTime":2,"prepaid":1,"topMoney":0,"topTime":0,"unlockCount":6,"endTime":1391},"l":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":0,"perMoney":0,"perTime":0,"prepaid":0,"topMoney":0,"topTime":0,"unlockCount":6,"endTime":1391}}}
        self.rm.run_main('put', set_pay_rule_url, data=json.dumps(set_pay_rule_data), header=dc.pc_headers('xiaodwx'))
        set_cabinet_url = 'http://debug2.wegui.cn/v1/cabinets/' + self.find_cabinet(cab_no)
        set_cabinet_data = {"passwordEnable":passwordEnable,"longRentEnable":longRentEnable,"shortRentEnable":shortRentEnable,"countRentEnable":countRentEnable,"type":type}
        cabinet_res = self.rm.run_main('put', set_cabinet_url, data=json.dumps(set_cabinet_data), header=dc.pc_headers('xiaodwx'))
        cabinet_config = cabinet_res['cabinetConfig']['objectId']
        set_cabinet_rule_url = 'http://debug2.wegui.cn/v1/cabinetConfigs/' + cabinet_config
        set_cabinet_rule_data = {"birthdayEnable":birthdayEnable,"idCardEnable":idCardEnable,"forcePhoneEnable":forcePhoneEnable}
        self.rm.run_main('put', set_cabinet_rule_url, data=json.dumps(set_cabinet_rule_data), header=dc.pc_headers('xiaodwx'))


    # 下单
    def xt_order(self, cab_no):
        order_url = 'https://azapi.wegui.cn/v1/orders'
        order_data = {"cabinetId":self.find_cabinet(cab_no),"rentType":"short","lockerType":"s","passwordEnable":False,"prepaid":1,"manualLockerEnable":True,"lockerId":"zxdG04YqEi"}
        order_res = self.rm.run_main('post', order_url, data=json.dumps(order_data), header=dc.wx_headers())
        return order_res['objectId']

    # 获取取件码
    def get_package_code(self, order_id):
        get_code_url = 'http://debug2.wegui.cn/v1/orderRecords?skip=0&limit=100&where={"order":{"__type":"Pointer","className":"Order","objectId":"' + order_id + '"}}&include=user'
        get_code_res = self.rm.run_main('get', get_code_url, header=dc.pc_headers('xiaodwx'))
        return get_code_res[0]['data']['password']


if __name__ == '__main__':
    pass
