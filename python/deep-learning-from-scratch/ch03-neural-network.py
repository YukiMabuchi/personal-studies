"""
ニューラルネットワーク:
適切な重みパラメータをデータから自動で学習できる
ニューラルネットワークは、パーセプトロンの欠点(期待する入力と出力をを満たすように適切な重みを極める作業が人の手によって行われる)を解消するためにある

パーセプトロンとニューラルネットワークの主な違いは、活性化関数がステップ関数かそれ以外(シグモイド関数、ReLU関数など)かの違い
"""

import numpy as np
import matplotlib.pylab as plt

"""
ステップ関数
0か1を返す
"""

# 実数用
# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0

# numpy用
# def step_function(x):
#     y = x > 0 # booleanの配列に変換
#     return y.astype(np.int) # int型に変換して返却

def step_function(x):
    return np.array(x > 0, dtype=np.intc)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1) # y軸の範囲を指定
# plt.show()

"""
シグモイド関数
実数を返す
"""
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1) # y軸の範囲を指定
# plt.show()


"""
ステップ関数もシグモイド関数も非線形関数
線形関数は、何かを入力した時に出力が入力の定倍数になり、1本の直線になる h(x) = cx

ニューラルネットワークには非線形関数を用いなければいけない
でないと多層にする利点が活かせない
"""

"""
ReLU関数
入力が0を超えていればその入力をそのまま、0以下なら0を出力
最近ではニューラルネットワークに用いられる
"""
def relu(x:int):
    return np.maximum(0, x)

"""
多次元配列
"""
# 1次元
A = np.array([1, 2, 3, 4])
print(np.ndim(A)) # 配列の次元数
print(A.shape) # 配列の形状
print(A.shape[0])

# 2次元 (行列)
B = np.array([[1, 2], [3, 4], [5, 6]])
print(np.ndim(B)) # 配列の次元数
print(B.shape) # 配列の形状 (3, 2) == 行数3 * 列数2の配列

# 行列の積
C = np.array([[1, 2], [3, 4]])
D = np.array([[5, 6], [7, 8]])
ml = np.dot(C, D) # Cの行 * Dの列 (1 * 5 + 2 * 7, 3 * 5 + 4 * 7などが列になる)
print(ml)

# 異なるshape間
E = np.array([[1, 2, 3], [4, 5, 6]])
F = np.array([[1, 2], [3, 4], [5, 6]])
ml = np.dot(E, F) # 2 * 3 と 3 * 2 の計算なので、一つ目のindex1と二つ目のindex0が同じ数値出ないといけない
print(ml) # 計算結果は一つ目の行数(index0)と二つ目の列数(index1)で構成される

# ニューラルネットワークの行列の積
# X = np.array([1, 2])
# W = np.array([[1, 3, 5], [2, 4, 6]])
# Y = np.dot(X, W)
# print(Y)

print('----------------------')

# ニューラルネットワークの各層の計算は行列の席でまとめて行える
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)

A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)
print(A1)
print(Z1)

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2  =np.array([0.1, 0.2])
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

# 恒等関数: 入力をそのまま出力する関数
# 出力層の活性化関数はケースに応じで選択する
def identity_function(x):
    return x

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3)
Y = identity_function(A3)

# ニューラルネットワーク実装のまとめ
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)


"""
出力層の設計
ニューラルネットワークは分類問題と回帰問題に分かれ、それぞれの出力層の活性化関数を使用する
回帰問題には恒等関数、分類問題にはソフトマックス関数
"""

# ソフトマックス関数、オーバーフローに気をつける
def softmax(a):
    c = np.max(a) # オーバーフロー対策
    exp_a = np.exp(a - c) # 指数関数
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

# ソフトマックス関数はの出力は0から1.0の間の実数になる。なので、確率として解釈できる
# 出力層のソフトマックス関数は省略するのが一般的

