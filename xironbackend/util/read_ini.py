# -*- coding: utf-8 -*-
import configparser


class ReadIni(object):

    def __init__(self, file_name=None, node=None):
        if file_name is None:
            self.file_name = "/Users/ranmenglong/workspace/github/xironbar/xironbackend/dataconfig/api.ini"
        else:
            self.file_name = file_name

        if node is None:
            self.node = "BaseUrl"
        else:
            self.node = node
        self.cf = self.load_ini(self.file_name)

    @staticmethod
    def load_ini(file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self, key=None):
        if key is None:
            key = 'base_url'
        return self.cf.get(self.node, key)

    def get_value_by_node_and_key(self, node, key):
        return self.cf.get(node, key)


if __name__ == '__main__':
    # read_init = ReadIni(node='ExcelPath')
    # print(read_init.get_value('sheet_id'))
    read_ini = ReadIni()
    data = read_ini.get_value_by_node_and_key('ExcelPath', 'file_path')
    print(data)
    valid_sheet_id = read_ini.get_value_by_node_and_key('ExcelPath', 'valid_sheet_id')
    print(valid_sheet_id)
    print(valid_sheet_id.split(','))
    print(type(valid_sheet_id.split(',')))
    for i in valid_sheet_id.split(','):
        print(i)
        print(type(i))
