import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('car.jpg', 0)

# 简单阈值（全局阈值，整幅图像采用同一个数作为阈值）
# ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # 如果像素值比阈值大，则设为最大值，否则，设为0
# ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # 如果像素值比阈值大，则设为0，否则，设为最大值
# ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)  # 如果像素值比阈值大，则设为最大值，否则，仍就是像素值
# ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)  # 如果像素值比阈值大，仍就是像素值，否则，设为0
# ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  # 如果像素值比阈值大，则设为0，否则，仍就是像素值
#
# titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
#
# for i in range(6):
#     plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()


# 自适应阈值(根据图像上的每一个小区域计算与其对应的阈值。)
# img = cv2.medianBlur(img, 5)
#
# ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # 全局阈值
# # 11为邻域大小， 2为一个常数，阈值就等于平均值或者加权平均值减去这个常数
# # 中值滤波
# th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#
# titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding',
#           'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
#
# for i in range(4):
#     plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()


# Otsu's 二值化（对一副双峰图像自动根据其直方图计算出一个阈值）
# 全局阈值
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Otsu's 阈值
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 进行高斯过滤后再使用Otsu's阈值，（5, 5）为高斯核的大小，0为标准差
blur = cv2.GaussianBlur(img, (5, 5), 0)
# 阈值一定要设为0
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding(v = 127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3])
    plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1])
    plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])

plt.show()
