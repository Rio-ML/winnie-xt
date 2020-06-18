import unittest


class ThirdCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始')

    @classmethod
    def tearDownClass(cls):
        print('结束')

    def setUp(self):
        print('执行每一条之前')

    def tearDown(self):
        print('执行每一条之后')

    # @unittest.skip('不执行')
    def test_001(self):
        print('这是001case')

    def test_002(self):
        print('这是002case')

    def test_003(self):
        print('这是003case')


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(ThirdCase('test_03_login_success'))
    # unittest.TextTestRunner().run(suite)
