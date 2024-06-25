"""
DOC: https://docs.python.org/3/library/doctest.html

簡単に見せたい時とかdocがわりなどに有効
ただ複雑なのは記述が長くなるため避けられる

functionのdocを各部分にテストを書く
>>>で対話型シェルのようにする
最後に期待値を書き、あっていれば何も返ってこない
"""

class Cal(object):
    def add_num_and_double(self, x, y):
        """Add and double

        >>> c = Cal()
        >>> c.add_num_and_double(1, 1)
        4

        >>> c.add_num_and_double('1', '1')
        Traceback (most recent call last):
        ...
        ValueError
        """
        
        if type(x) is not int or type(y) is not int:
            raise ValueError
        
        return (x + y) * 2

if __name__ == '__main__':
    import doctest
    doctest.testmod()