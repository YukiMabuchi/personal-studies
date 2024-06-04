"""
パーセプトロン:
複数の信号を入力として受け取り、一つの信号を出力する(1 or 2)
入力信号はニューロンんい送られる際に固有の重みが乗算される
信号の総和が計算され、それがある限界値(閾値)を超えた場合にのみ1を出力する
"""
import numpy as np


"""
パーセプトロンの実装
y = { 0 (w1x1 + w2x2 <= θ)
      1 (w1x2 + w2x2 > θ)
"""

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
# print(AND(0, 0))
# print(AND(1, 0))
# print(AND(0, 1))
# print(AND(1, 1))

"""
重みとバイアス
y = { 0 (b + w1x1 + w2x2 <= 0)
      1 (b + w1x2 + w2x2 > 0)

重み: 入力信号への重要度をコントロールするパラメータ
バイアス: 出力信号が1を出力する度合いを調整するパラメータ
"""

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7 # 元theta

print(np.sum(w*x) + b)

# 重みとバイアスの導入
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

"""
多層パーセプトロン
XORは多層パーセプトロンで表現する
"""

# XORはNANDとORをANDで見る、多層パーセプトロン
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    
    y = AND(s1, s2)
    return y


