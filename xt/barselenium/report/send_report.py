# -*- coding: utf-8 -*-
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from case import table

now = time.strftime("%Y-%m-%d_%H_%M_%S")
path = "Test Report " + now + '.html'
report_file = 'E:\\xt\\barselenium\\report\\' + path
report_title = u'Example用例执行报告'
desc = u'订台'
# suite = unittest.main()
suite = unittest.TestSuite()
suite.addTest(table.TestOpenReserveTable("test_001"))
# suite.addTest(unittest_case.TestReserveTable("test_002"))

with open(report_file, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title=report_title, description=desc, verbosity=2)
    runner.run(suite)
