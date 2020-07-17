from util.operation_excel import OperationExcel
from data import data_config
from util.operation_json import OperationJson


class GetData:
    def __init__(self, file_name=None, sheet_id=None):
        self.operation_excel = OperationExcel(file_name, sheet_id)

    # 获取Excel行数，即case个数
    def get_case_lines(self):
        return self.operation_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        col = int(data_config.get_run())
        run_model = self.operation_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 如果excel里是 yes or no 来判断是否携带header
    def is_header(self, row):
        col = int(data_config.get_header())
        header = self.operation_excel.get_cell_value(row, col)
        if header == 'yes':
            return data_config.get_login_header_value()
        else:
            return None

    # 如果excel表里header是用户名
    def get_header(self, row):
        col = int(data_config.get_header())
        header = self.operation_excel.get_cell_value(row, col)
        pc_headers = data_config.pc_headers(header)
        return pc_headers

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_request_method())
        request_method = self.operation_excel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_url(self, row):
        col = int(data_config.get_url())
        url = self.operation_excel.get_cell_value(row, col)
        return url

    # 获取前提条件--返回结果数据
    def get_pre_data(self, row):
        col = int(data_config.get_pre())
        data = self.operation_excel.get_cell_value(row, col)
        return data

    # 获取请求数据
    def get_request_data(self, row):
        col = int(data_config.get_data())
        data = self.operation_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expect_data(self, row):
        col = int(data_config.get_expect())
        expect = self.operation_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    def get_case_id(self, row):
        col = int(data_config.get_id())
        case_id = self.operation_excel.get_cell_value(row, col)
        if case_id == '':
            return None
        return case_id

    def write_result(self, row, value):
        col = int(data_config.get_result())
        self.operation_excel.write_value(row, col, value)

    def write_res_to_pre(self, row, value):
        col = int(data_config.get_pre())
        # 请求 res.json()方法会把 null 转换成 None 破坏 json格式，这里回写 excel时将 None用引号包裹
        self.operation_excel.write_value(row, col, value.replace("None", "null"))

    # 判断是否有case依赖
    def get_case_depend(self, row):
        col = int(data_config.get_case_depend())
        case_depend = self.operation_excel.get_cell_value(row, col)
        if case_depend == "":
            return None
        else:
            return case_depend

