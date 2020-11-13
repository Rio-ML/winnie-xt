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