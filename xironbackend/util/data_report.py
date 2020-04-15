import requests
import json
import time
from jsonpath_rw import jsonpath,parse

# url = 'http://berry-server.wegui.cn/areas/'
# # data = {"name": "dxs 1"}
# header = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Token 9ee03b6126796e6b7c279e361fa3b1770baf68ec',
#         'X-CSRFToken': 'ZO3XOS7Rwg1CM8pIGqQgsSLGAEGKBRCWkuoyMT3VWE3aimOxzblRwQM5PBd2MEsS'
#     }
# # res = requests.get(url=url, params=data, headers=header)
# res = requests.get(url=url, headers=header)
# res_result = res.json()['results']
# for item in res_result:
#     print(item['id'])
#     url_del = 'http://berry-server.wegui.cn/areas/{id}/'
#     url_delete = url_del.replace('{id}', item['id'])
#     print(url_delete)
#     res = requests.delete(url=url_delete, headers=header)

url = 'http://berry-server.wegui.cn/areas/2ac99fe4-d363-4c26-b4aa-024d57c84a0b/'
data = {"name": "dxs"}
header = {
        'Content-Type': 'application/json',
        'Authorization': 'Token 9ee03b6126796e6b7c279e361fa3b1770baf68ec',
        'X-CSRFToken': 'ZO3XOS7Rwg1CM8pIGqQgsSLGAEGKBRCWkuoyMT3VWE3aimOxzblRwQM5PBd2MEsS'
    }
# res = requests.get(url=url, params=data, headers=header)
res = requests.put(url=url, data=data, headers=header)

print(res.json())

#
#
# str = 'abcd:efghijk'
# print(str.startswith('abc'))
# print(str.split(':')[1])

# str = '{"errors": [{"message": "Area with this \u9152\u5427 and \u533a\u57df\u540d already exists.", "code": "invalid", "field": "__all__"}]}'
# aa = '{"errors": [{"message": "Area with this 酒吧 and 区域名 already exists.", "code": "invalid", "field": "__all__"}]}'
# print(str == aa)


# a = 'http://berry-server.wegui.cn/areas/{id}/'
# b = a.replace('{id}', '111111111')
# print(b)

# url_payrule = 'http://debug2.wegui.cn/v1/cabinets/3ZMmzgj7jT/payRule'
# url_command = 'http://debug2.wegui.cn/v1/cabinets/3ZMmzgj7jT/commands'
# data_payrule = {"forgetPayRule":{"s":{"prepaid":0},"m":{"prepaid":0},"l":{"prepaid":0}},"payRule":{"s":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":0,"perMoney":5,"perTime":20,"prepaid":500,"topMoney":0,"topTime":0,"unlockCount":0,"endTime":0},"m":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":0,"perMoney":0,"perTime":0,"prepaid":0,"topMoney":0,"topTime":0,"unlockCount":0,"endTime":0},"l":{"beforeMoney":0,"beforeTime":0,"freeTime":0,"owingTime":0,"perMoney":0,"perTime":0,"prepaid":0,"topMoney":0,"topTime":0,"unlockCount":0,"endTime":0}}}
# data_command = {"cmd":"update_info","data":{}}
# header = {'Content-Type': 'application/json', 'Xi-App-Id': '0a8020002101b2ddc7626fca179adf70', 'Xi-Session-Token': 'r:8b4170e8abc54e7172d66d33f1424249'}

# res_payrule = requests.put(url=url_payrule, data=json.dumps(data_payrule), headers=header)
# res_payrule = requests.put(url=url_payrule, json=data_payrule, headers=header)

# res_command = requests.post(url=url_command, data=json.dumps(data_command), headers=header)
