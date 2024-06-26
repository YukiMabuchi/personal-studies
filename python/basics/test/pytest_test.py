"""
DOC: https://docs.pytest.org/en/8.2.x/getting-started.html#get-started
     https://docs.pytest.org/en/8.2.x/how-to/index.html#how-to
     
python3 -m pytest python/basics/test/pytest_test.py -s
conftestでoptionを追加するならファイル名の後に
print結果の出力は-sオプション
標準ライブラリのunittestのコードも実行できる
class名はTestからはじめる、テスト用関数の名前はtest_から始める
setup, teardownのclassを用いることで毎回処理をせずにテスト時一回ずつのみ実行される

テストのカバレッジを確認するにはpytest-covでtestパスとtest対象を確認
python3 -m pytest python/basics/test/pytest_test.py --cov unittest_
"""
import os
import shutil
import pytest

import unittest_

version = 1

class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = unittest_.Cal()
        cls.test_dir = '/tmp/test_dir'
        cls.test_file_name = 'test.txt'
    
    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)
    
    def setup_method(self, method):
        print(f'method={method.__name__}')
        # self.cal = unittest_.Cal()

    def teardown_method(self, method):
        print(f'method={method.__name__}')
        # del self.cal
    
    # @pytest.mark.skip(reason='skip!')
    # @pytest.mark.skipif(version==1, reason='skip!')
    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        print(os_name)
        assert self.cal.add_num_and_double(1, 1) == 4

    # 例外チェック
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
    
    def test_save(self, tmpdir, csv_file):
        print(csv_file)
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True
    
    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path) is True