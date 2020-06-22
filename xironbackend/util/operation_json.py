import json


class OperationJson:
    def __init__(self):
        self.data = self.read_data()

    # 读取 login data json 文件
    @staticmethod
    def read_data():
        # location = '/Users/ranmenglong/workspace/github/xironbar/xironbackend/dataconfig/loginjson.json'
        # location = 'E:/xt/xironbardepend/xironbackend/dataconfig/table.json'
        location = 'E:/xt/xtcontract/xironbackend/dataconfig/payrule.json'
        with open(location, 'r', encoding='UTF-8') as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, id):
        if id:
            return self.data[id]
        else:
            return None


if __name__ == '__main__':
    opjson = OperationJson()

