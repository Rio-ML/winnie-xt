import requests
import jsonpath
import json
from api.data import data_config as dc
from api.Base.runmethod import RunMethod


'''
小铁备忘录
'''


class IronMemo():
    def __init__(self):
        self.rm = RunMethod()

    # 获取到json中任意key的值,结果为list格式
    def get_json_value(self, json_data, key_name):
        key_value = jsonpath.jsonpath(json_data, '$..{key_name}'.format(key_name=key_name))
        # key_value = jsonpath.jsonpath(json_data, '$..' + key_name + "'")
        # key_value = jsonpath.jsonpath(json_data, '$..{}'.format(key_name))
        return key_value

    # 增加 N 个备忘录
    def add_memorandum(self, title, num):
        ad_m_url = 'http://debug2.wegui.cn/v1/memorandums'
        ad_m_data = {"title": title, "content": "啦啦啦啦啦啦啦啦啦啦啦啦", "type": "rule",
                     "reminders": [{"id": "5D5iZ5TSf1", "username": "xd150", "nickname": "2", "phone": "22222222222"}],
                     "remindAt": {"__type": "Date", "iso": "2020-07-15T07:00:00.000Z"}}

        for i in range(1, num):
            add_memo_res = self.rm.run_main('post', ad_m_url, data=json.dumps(ad_m_data), header=dc.pc_headers('xiaod'))
            i += 1
            print("增加备忘录内容：" + add_memo_res['title'])

    # 批量取消备忘录
    def cancel_memorandum(self, num):
        for i in range(1, num):
            # 获取备忘录列表
            m_url = 'http://debug2.wegui.cn/v1/memorandums?limit=1&skip=0&order=-status,-createdAt&include=user,operator&where=%7B%7D'
            m_list_res = self.rm.run_main('get', m_url, header=dc.pc_headers('xiaod'))
            # 获取备忘录id(两种方法)
            # memo_id = IronMemo().get_json_value(memo_list_res, "objectId")[0]
            m_id = m_list_res[0]["objectId"]
            # 取消目标备忘录
            upd_m_url = 'http://debug2.wegui.cn/v1/memorandums/' + m_id
            m_state_data = {"status": "cancel", "remark": ""}
            upd_m_res = self.rm.run_main('put', upd_m_url, data=json.dumps(m_state_data), header=dc.pc_headers('xiaod'))
            i += 1
            print("取消备忘录内容：" + upd_m_res['title'])


if __name__ == '__main__':
    # IronMemo().cancel_memorandum(2)
    IronMemo().add_memorandum('mymameisdxs', 2)



