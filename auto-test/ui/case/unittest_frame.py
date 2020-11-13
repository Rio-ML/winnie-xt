import unittest


class SecondCase(unittest.TestCase):
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
    def test_01(self):
        print('这是01case')

    def test_02(self):
        print('这是02case')

    def test_03(self):
        print('这是03case')


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(SecondCase('test_03_login_success'))
    # unittest.TextTestRunner().run(suite)
