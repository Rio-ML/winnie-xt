# -*- coding: utf-8 -*-
from api.Base.runmethod import RunMethod
from api.data.get_data import GetData
from api.data.dependent_data import DependentData
from api.util.send_email import SendEmail
from api.util.read_ini import ReadIni

import json
import unittest


class RunTest(unittest.TestCase):
    def __init__(self):
        unittest.TestCase.__init__(self)
        xiao_iron = 'E:/xt/xironbardepend/xironbackend/'
        self.run_method = RunMethod()
        self.data = GetData(xiao_iron + 'dataconfig/interfacebar1.xlsx', 2)
        self.send_mai = SendEmail()
        self.read_int = ReadIni()

    # 程序执行的
    def go_on_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        success_count = 0
        fail_count = 0
        total_count = 0
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.read_int.get_value() + self.data.get_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                header = self.data.get_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case is not None:
                    self.depend_data = DependentData(depend_case)
                    # 获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    if depend_key is None:  # 如果依赖字段为空，则替换 url 中的{id}
                        url = url.replace('{id}', depend_response_data)
                    else:  # 如果依赖字段有值，则更改请求字段对应的 depend_key 的 value为依赖请求的结果
                        request_data[depend_key] = depend_response_data
                if method != 'get':
                    request_data = json.dumps(request_data)
                total_count += 1
                res = self.run_method.run_main(method, url, request_data, header)
                expect_res_str = self.data.get_expect_data(i).__str__()
                if expect_res_str is not None:
                    expect_res_list = expect_res_str.split('/')
                    all_expect_pass = True
                    for a in expect_res_list:
                        # 断言报错继续执行
                        try:
                            # self.assertIn(self.data.get_expect_data(i), json.dumps(res), "返回结果不是期望结果")
                            # 因为返回结果中不会有中文，所以将期望值的中文转成 Unicode 的 byte ，为了匹配 assertIn 的参数类型，再转成 utf-8的str
                            self.assertIn(a.encode("unicode_escape").decode('utf-8'), json.dumps(res), "返回结果不是期望结果")
                            print("用例编号：", self.data.get_case_id(i), ",接口自动化测试通过")
                            self.data.write_result(i, 'pass')
                        except AssertionError as e:
                            print("用例编号：", self.data.get_case_id(i), ",接口自动化测试失败!!!\n", "断言异常为：", e)
                            self.data.write_result(i, 'fail' + e.__str__().encode("utf-8").decode('utf-8'))
                            # fail_count += 1
                            all_expect_pass = False
                    if all_expect_pass:
                        success_count += 1
                    else:
                        fail_count += 1
                else:
                    # 断言报错继续执行
                    try:
                        self.assertEqual(res.status_code, 204, '该操作不成功，无返回结果')
                        print("用例编号：", self.data.get_case_id(i), ",接口自动化测试通过")
                        self.data.write_result(i, 'pass')
                        success_count += 1
                    except AssertionError as e:
                        print("用例编号：", self.data.get_case_id(i), ",接口自动化测试失败!!!\n", "断言异常为：", e)
                        self.data.write_result(i, 'fail' + e.__str__())
                        fail_count += 1
                if type(res) is not dict:
                    self.data.write_res_to_pre(i, res.__str__().encode("utf-8").decode('utf-8'))
                else:
                    # self.data.write_res_to_pre(i, json.dumps(res))
                    # 回写 excel时，通过json.dumps() 会将中文编译成 Unicode，这里直接处理成 str
                    # 结果回写需要是 json格式，将单引号换成双引号
                    pre_json = res.__str__().replace('\'', '\"')
                    self.data.write_res_to_pre(i, pre_json)
        print("本次接口自动化测试运行用例总数：", total_count)
        print("本次接口自动化测试通过用例数：", success_count)
        print("本次接口自动化测试失败用例数：", fail_count)

        # self.send_mai.send_main(success_count, fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()


