import json
from xironbackend.data.Dict import Dict


class CommonUtil:
    @staticmethod
    def is_contain(str_one, str_two):
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    # 判断是否为 json 格式
    @staticmethod
    def is_json(value):
        try:
            json.loads(value)
        except ValueError:
            return False
        return True

    # 转换字典成为对象，可以用"."方式访问对象属性
    @staticmethod
    def dict_to_object(dict_obj):
        if not isinstance(dict_obj, dict):
            return dict_obj
        inst = Dict()
        for k, v in dict_obj.items():
            inst[k] = CommonUtil.dict_to_object(v)
        return inst


