# a = list()
# a.append('aa')
# a.append('qqq')
# print(a)
# print('aa' in a)


# from api.data.Dict import Dict
# import json
#
#
# def dict_to_object(dict_obj):
#     if type(dict_obj) is list:
#         for item in dict_obj:
#             if not isinstance(item, dict):
#                 # return item
#                 dict_obj.append(item)
#                 continue
#             inst = Dict()
#             for k, v in item.items():
#                 inst[k] = dict_to_object(v)
#                 dict_obj.append(inst)
#         return dict_obj
#
#
# a = json.loads('[{"dp_case_id":"agent-test-001","dp_key":"id","fit_field":null}]')
# dict_to_object(a)

# class Demo:
#     def __init__(self):
#         self.data = '111'
#
#     def run(self):
#         print(self.data)
#
#
# if __name__ == '__main__':
#     demo = Demo()
#     demo.run()
#     print(demo.data)

# import configparser
#
#
# class ReadIni(object):
#
#     def __init__(self, file_name=None, node=None):
#         if file_name is None:
#             file_name = "/Users/ranmenglong/workspace/githubxironbar/xironbackend/dataconfig/api.ini"
#         if node is None:
#             self.node = "BaseUrl"
#         else:
#             self.node = node
#         self.cf = self.load_ini(file_name)
#
#     def load_ini(self, file_name):
#         cf = configparser.ConfigParser()
#         cf.read(file_name)
#         return cf
#
#     def get_value(self, key=None):
#         if key is None:
#             key = 'base_url'
#         data = self.cf.get(self.node, key)
#         return data
#
#
# if __name__ == '__main__':
#     read_init = ReadIni(node='ExcelPath')
#     print(read_init.get_value('sheet_id'))
# for i in range(1, 8):
#     list = [1, 2, 4]
#     if i == 3 and i in list:
#         list.remove(i)
#         print(list)
#         i += 1
#     else:
#         print("ddddd")
#         i += 1
import json
import jsonpath
data = {
    "duringTime": 401,
    "timesPerDay": 10000,
    "device":{
        "appid":1,
        "appName":"com.planet2345.com",
        "appName2":"com.planet2345.com2"
    }
}


def get_json_value(json_data, key_name):
    '''获取到json中任意key的值,结果为list格式'''
    key_value = jsonpath.jsonpath(json_data, '$..{key_name}'.format(key_name=key_name))
    # key的值不为空字符串或者为empty（用例中空固定写为empty）返回对应值，否则返回empty

    return key_value


if __name__ == '__main__':
    a = get_json_value(data, 'appid')
    print(a)