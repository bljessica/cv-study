import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('car.jpg')

# 2D卷积
# 均值滤波器
# kernel = np.ones((5, 5), np.float32) / 25
#
# # -1为目标图像所需的深度，为-1表示输出图像与输入图像有相同的深度（图像深度是指像素深度中实际用于存储图像的灰度或色彩所需要的比特位数）
# dst = cv2.filter2D(img, -1, kernel)
#
# plt.subplot(121), plt.imshow(img), plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122, ), plt.imshow(dst), plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()


# 图像模糊（图像平滑）
# 平均
# blur = cv2.blur(img, (5, 5))
# 高斯模糊（卷积核换成高斯核，原来的求平均数现在变成求加权平均数）
# blur = cv2.GaussianBlur(img, (5, 5), 0)
# 中值模糊
# blur = cv2.medianBlur(img, 5)
# 双边滤波（能在保持边界清晰的情况下有效的去除噪音）
# 9 邻域直径，两个 75 分别是空间高斯函数标准差，灰度值相似性高斯函数标准差
blur = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
