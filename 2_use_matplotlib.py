import cv2
from matplotlib import pyplot as plt

img = cv2.imread('car.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # 隐藏坐标轴标记
# 彩色图像使用 OpenCV 加载时是 BGR 模式。但是 Matplotib 是 RGB模式。
# 所以彩色图像如果已经被 OpenCV 读取，那它将不会被 Matplotib 正确显示
plt.show()
