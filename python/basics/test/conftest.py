"""
pytestはtestファイルと同じdirにconftestがあれば参照する
addoptionに入ったものはテスト用関数のrequestという引数に入れられる
@pytest.fixtureでカスタムでテスト用関数の引数を作れる
"""
import os
import pytest

@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir, 'test.csv'), 'w+') as c:
        yield c # yieldを使うと、fixtureの中でcloseするから便利

def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')