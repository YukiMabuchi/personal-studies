"""
DOC: https://docs.python.org/3/library/unittest.html

unittest.TestCaseを継承しテストができる
テスト用関数の名前はtest_から始める
setUpとtearDownで各テストfunctionが実行される前と後にそれぞれ処理を行える
@unittest.skipデコレーターでテストをスキップできる
"""

import unittest

import unittest_

version = 1

class CalTest(unittest.TestCase):
    def setUp(self):
        print('set up')
        self.cal = unittest_.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal
    
    # @unittest.skip('skip!')
    @unittest.skipIf(version==1, 'skip for version 1')
    def test_add_num_and_double(self):
        self.assertEqual(
            self.cal.add_num_and_double(1, 1),
            4
        )
    
    # 例外チェック
    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')

if __name__ == '__main__':
    unittest.main()