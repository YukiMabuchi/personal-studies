"""
DOC: https://docs.python.org/3/library/pickle.html

The pickle module implements binary protocols for serializing and de-serializing a Python object structure. 
Pythonでのみ使用可能なので他言語と互換性がない点に注意
"""

import pickle

class T(object):
    def __init__(self, name):
        self.name = name

data = {
    'a': [1, 2, 3],
    'b': ('test', 'test'),
    'c': {'key': 'value'},
    'd': T('test')
}

with open('python/basics/db/pickle_data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('python/basics/db/pickle_data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(data_loaded)