import unittest
import os


class RunCase(unittest.TestCase):
    def test_case01(self):
        # case_path = os.path.join(os.getcwd(), 'case')    # windows可以使用，mac报错
        case_path = os.path.abspath(os.path.dirname(__file__))  # 要获取当前文件所在文件夹的目录，才能让TestLoader扫描当前目录下的文件
        print(case_path)
        suite = unittest.defaultTestLoader.discover(case_path, 'unittest_*.py')
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()
