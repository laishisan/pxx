import unittest


class UserTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupClass开始")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass 资源清理")

    def testCase1(self):
        print("test  Case1")

    def testCase2(self):
        print("test Case2")
        self.assertEqual(1, 1)

    @unittest.skip("跳过这个")
    def testCase3(self):
        print("test Case3")
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
