# Canny边缘检测原理
# 1.噪声去除
# 2.计算图像梯度（对平滑后的图像使用 Sobel 算子计算水平方向和竖直方向的一阶导数，找到边界的梯度和方向）
# 3.非极大值抑制（对整幅图像做一个扫描，去除那些非边界上的点。对每一个像素进行检查，看这个点的梯度是不是周围具有相同梯度方向的点中最大的。）
# 滞后阈值（现在要确定那些边界才是真正的边界。这时我们需要设置两个阈值：minVal 和 maxVal。
# 当图像的灰度梯度高于 maxVal 时被认为是真的边界，那些低于 minVal 的边界会被抛弃。
# 如果介于两者之间的话，就要看这个点是否与某个被确定为真正的边界点相连，如果是就认为它也是边界点，如果不是就抛弃）

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('car.jpg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
