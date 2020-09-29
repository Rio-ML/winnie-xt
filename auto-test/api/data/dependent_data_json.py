from api.util.operation_excel import OperationExcel
from api.data.get_data import GetData
import json
from api.util.read_ini import ReadIni
from api.util.common_util import CommonUtil


class DependentDataJson:
    def __init__(self, excel_prop):
        self.excel_prop = excel_prop
        self.opera_excel = OperationExcel()
        xiao_iron = 'E:/xt/winnie-xt/auto-test/api/'
        self.data = GetData(xiao_iron + 'dataconfig/interfacebar1.xlsx', 8)
        self.read_ini = ReadIni()

    # 组装执行请求需要的数据，组装 excel_prop
    def assemble_excel_prop(self):
        case_depend_list = json.loads(self.excel_prop.case_depend)
        for case_depend in case_depend_list:
            case_depend_obj = CommonUtil.dict_to_object(case_depend)
            case_dp_value = self.get_pre_data_for_case_and_key(case_depend_obj.dp_case_id, case_depend_obj.dp_key)
            if case_depend_obj.fit_field is not None:
                if 'data_type' in case_depend_obj.keys() and case_depend_obj.data_type == 'list':
                    fit_field_value_list = list()
                    fit_field_value_list.append(case_dp_value)
                    self.excel_prop.request_data[case_depend_obj.fit_field] = fit_field_value_list
                else:
                    self.excel_prop.request_data[case_depend_obj.fit_field] = case_dp_value
            else:
                # 填充数据为空的时候，需要直接填充到 url 上
                self.excel_prop.url = self.excel_prop.url.replace('{' + case_depend_obj.dp_key + '}', case_dp_value)

        return self.excel_prop

    # 通过 case_id dp_key,获取前置数据中 dp_key对应的值
    def get_pre_data_for_case_and_key(self, case_id, dp_key):
        row_num = self.opera_excel.get_row_num(case_id)
        pre_data = json.loads(self.data.get_pre_data(row_num))  # pre_data 是直接从 excel中读取，不用通过 json的 key获取
        return self.dict_get(pre_data, dp_key, None)

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
