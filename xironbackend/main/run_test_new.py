# -*- coding: utf-8 -*-
from Base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.send_email import SendEmail
from util.read_ini import ReadIni
from data.dependent_data_json import DependentDataJson
from data.Dict import Dict

import json
import unittest


class RunTest(unittest.TestCase):
    def __init__(self):
        unittest.TestCase.__init__(self)
        xiao_iron = 'E:/xt/xtcontract/xironbackend/dataconfig/'
        self.run_method = RunMethod()
        self.data = GetData(xiao_iron + 'interfacebar1.xlsx', 7)
        self.send_mai = SendEmail()
        self.read_int = ReadIni()
        self.statistic = Dict()
        self.excel_prop = Dict()

    # 程序执行的
    def go_on_run(self):
        self.excel_prop.rows_count = self.data.get_case_lines()
        self.statistic.success_count = 0
        self.statistic.fail_count = 0
        self.statistic.total_count = 0
        for i in range(2, self.excel_prop.rows_count):
            self.excel_prop.index = i
            self.excel_prop.is_run = self.data.get_is_run(i)
            if self.excel_prop.is_run:
                self.excel_prop.url = self.read_int.get_value() + self.data.get_url(i)
                self.excel_prop.method = self.data.get_request_method(i)
                self.excel_prop.request_data = self.data.get_data_for_json(i)
                self.excel_prop.header = self.data.get_header(i)
                self.excel_prop.case_depend = self.data.get_case_depend(i)
                if self.excel_prop.case_depend is not None and CommonUtil.is_json(self.excel_prop.case_depend):
                    self.depend_data_json = DependentDataJson(self.excel_prop)
                    self.excel_prop = self.depend_data_json.assemble_excel_prop()
                if self.excel_prop.method != 'get':
                    self.excel_prop.request_data = json.dumps(self.excel_prop.request_data)
                self.statistic.total_count += 1
                res = self.run_method.run_main(self.excel_prop.method, self.excel_prop.url,
                                               self.excel_prop.request_data, self.excel_prop.header)
                self.excel_prop.expect_res_str = self.data.get_expect_data(i).__str__()
                if self.excel_prop.expect_res_str is not None:
                    expect_res_list = self.excel_prop.expect_res_str.split('/')
                    all_expect_pass = True
                    for expect_res in expect_res_list:
                        # 断言报错继续执行
                        try:
                            # 因为返回结果中不会有中文，所以将期望值的中文转成 Unicode 的 byte ，为了匹配 assertIn 的参数类型，再转成 utf-8的str
                            self.assertIn(expect_res.encode("unicode_escape").decode('utf-8'),
                                          json.dumps(res), "返回结果不是期望结果")
                            print("用例编号：", self.data.get_case_id(i), ",接口自动化测试通过")
                            self.data.write_result(i, 'pass')
                        except AssertionError as e:
                            print("用例编号：", self.data.get_case_id(i), ",接口自动化测试失败!!!\n", "断言异常为：", e)
                            self.data.write_result(i, 'fail' + e.__str__().encode("utf-8").decode('utf-8'))
                            # self.statistic.fail_count += 1
                            all_expect_pass = False
                    if all_expect_pass:
                        self.statistic.success_count += 1
                    else:
                        self.statistic.fail_count += 1
                else:
                    # 断言报错继续执行
                    try:
                        self.assertEqual(res.status_code, 204, '该操作不成功，无返回结果')
                        print("用例编号：", self.data.get_case_id(i), ",接口自动化测试通过")
                        self.data.write_result(i, 'pass')
                        self.statistic.success_count += 1
                    except AssertionError as e:
                        print("用例编号：", self.data.get_case_id(i), ",接口自动化测试失败!!!\n", "断言异常为：", e)
                        self.data.write_result(i, 'fail' + e.__str__())
                        self.statistic.fail_count += 1
                if type(res) is not dict:
                    self.data.write_res_to_pre(i, res.__str__().encode("utf-8").decode('utf-8'))
                else:
                    # 回写 excel时，通过json.dumps() 会将中文编译成 Unicode，这里直接处理成 str
                    # 结果回写需要是 json格式，将单引号换成双引号
                    pre_json = res.__str__().replace('\'', '\"')
                    self.data.write_res_to_pre(i, pre_json)
        print("本次接口自动化测试运行用例总数：", self.statistic.total_count)
        print("本次接口自动化测试通过用例数：", self.statistic.success_count)
        print("本次接口自动化测试失败用例数：", self.statistic.fail_count)

        # self.send_mai.send_main(success_count, self.statistic.fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()


