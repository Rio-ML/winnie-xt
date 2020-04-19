from xironbackend.util.operation_excel import OperationExcel
from xironbackend.Base.runmethod import RunMethod
from xironbackend.data.get_data import GetData
import json
from xironbackend.util.read_ini import ReadIni


class DependentData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        xiao_iron = '/Users/ranmenglong/workspace/github/xironbar/xironbackend/'
        self.data = GetData(xiao_iron + 'dataconfig/interfacebar1.xlsx', 2)
        self.read_ini = ReadIni()

    # 通过 caseid 去获取该 caseID 的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.get_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.read_ini.get_value() + self.data.get_url(row_num)
        res = run_method.run_main(method, url, request_data, header)
        return res

    # 根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row)
        is_pre_start = depend_data.startswith('pre:')
        if is_pre_start:
            depend_key = depend_data.split(':')[1]
            return self.get_pre_data(depend_key)
        else:
            response_data = self.run_dependent()
            res = self.dict_get(response_data, depend_data, None)
            return res

    def get_pre_data(self, depend_key):
        row_num = self.opera_excel.get_row_num(self.case_id)
        pre_data = json.loads(self.data.get_pre_data(row_num))  # pre_data 是直接从 excel中读取，不用通过 json的 key获取
        res = pre_data[depend_key]
        return res

    # 获取字典中的objkey对应的值，适用于字典嵌套
    # dict:字典 objkey:目标key default:找不到时返回的默认值
    def dict_get(self, _dict, key, default):
        tmp = _dict
        for k, v in tmp.items():
            if k == key:
                return v
            else:
                if isinstance(v, list):
                    for item in v:
                        ret = self.dict_get(item, key, default)
                        if ret is not default:
                            return ret
                elif isinstance(v, dict):
                    ret = self.dict_get(v, key, default)
                    if ret is not default:
                        return ret
        return default


