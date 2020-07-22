import requests
import jsonpath
import json
from jsonpath_rw import jsonpath, parse

# url = 'http://debug2.wegui.cn/v1/memorandums'
# data = {"title":"autotest","content":"啦啦啦啦啦啦啦啦啦啦啦啦","type":"rule","reminders":[{"id":"5D5iZ5TSf1","username":"xd150","nickname":"2","phone":"22222222222"}],"remindAt":{"__type":"Date","iso":"2020-07-15T07:00:00.000Z"}}
# header = {
#         'Content-Type': 'application/json',
#         'Xi-App-Id': '0a8020002101b2ddc7626fca179adf70',
#         'Xi-Session-Token': 'r:ee14f0d8fd77040364c7ac63ec443355'
#     }
# # res = requests.post(url=url, data=json.dumps(data), headers=header)
# # print(res)
#
# for i in range(1, 500):
#     res = requests.post(url=url, data=json.dumps(data), headers=header)
#     i += 1
#     print(res)


def get_json_value(json_data, key_name):
    #获取到json中任意key的值,结果为list格式ba
    key_value = jsonpath.jsonpath(json_data, '$..{key_name}'.format(key_name=key_name))
    # key_value = jsonpath.jsonpath(json_data, '$..' + key_name + "'")
    # key_value = jsonpath.jsonpath(json_data, '$..{}'.format(key_name))
    return key_value


for i in range(1, 2):
    url1 = 'http://debug2.wegui.cn/v1/memorandums?limit=1&skip=0&order=-status,-createdAt&include=user,operator&where=%7B%7D'
    header = {
            'Content-Type': 'application/json',
            'Xi-App-Id': '0a8020002101b2ddc7626fca179adf70',
            'Xi-Session-Token': 'r:ee14f0d8fd77040364c7ac63ec443355'
        }
    res1 = requests.get(url=url1, headers=header)
    a = res1.json()
    b = get_json_value(a, "objectId")[0]
    data = {"status": "cancel", "remark": ""}
    url2 = 'http://debug2.wegui.cn/v1/memorandums/' + b
    res2 = requests.put(url=url2, data=json.dumps(data), headers=header)
    print(res2)
    i += 1



