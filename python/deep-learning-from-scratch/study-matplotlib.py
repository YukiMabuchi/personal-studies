import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.image import imread

"""
例1
"""
# x = np.arange(0, 6, 0.1) # 0から6まで0.1刻みで生成
# y = np.sin(x)

# plt.plot(x, y)
# plt.show()

"""
例2
"""
# x = np.arange(0, 6, 0.1) # 0から6まで0.1刻みで生成
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, label="sin")
# plt.plot(x, y2, linestyle="--", label="cos")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("sin & cos")
# plt.legend()
# plt.show()

"""
画像表示
"""
img = imread("./python/deep-learning-from-scratch/sample.jpeg")
plt.imshow(img)

plt.show()