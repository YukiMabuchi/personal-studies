"""
This file is for studying numpy lib

Datatypes doc:
https://numpy.org/doc/stable/user/basics.types.html
"""

import numpy as np


"""
numpy array
要素ごと(element-wise)の計算
"""
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
# print(x * y)

"""
ブロードキャスト(後述)
単一の数値(スカラ値)との計算
"""
x = np.array([1.0, 2.0, 3.0])
# print(x / 2.0)

"""
N次元配列
1次元配列はベクトル、2次元配列は行列、それらを一般化したものはテンソルと呼ぶ
"""
A = np.array([[1, 2], [3, 4]])
# print(A)
# print(A.shape)
# print(A.dtype)
# element-wiseもスカラ値との計算も可能

"""
ブロードキャスト
スカラ値を計算対象の配列の形に拡張されて計算される
[1, 2] * 10だと、[1, 2] * [10, 10]で計算される
"""

"""
要素へのアクセス
"""
X = np.array([[51, 55], [14, 19], [0, 4]])

# 普通のindexと同じ
# print(X[0])

# 各要素へのアクセス
Y = X.flatten() # N次元配列を1次元配列に変換
print(X)
print(Y)
print(Y[np.array([0, 2, 4])]) # indexが0, 2, 4の要素を取得
Y > 15 # booleanの配列が返却される
print(Y[Y > 15]) # 条件も指定可能

