import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('car.jpg')

# 扩展缩放
# # None 本应该是输出图像的尺寸，但是因为后边设置了缩放因子，因此这里为 None
# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
#
# # or
# # height, width = img.shape[:2]
# # res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
#
# while 1:
#     cv2.imshow('res', res)
#     cv2.imshow('img', img)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cv2.destroyAllWindows()


# 平移
# rows, cols = img.shape[:2]
#
# # 定义平移矩阵（沿x方向50，y方向100）
# M = np.float32([[1, 0, 50], [0, 1, 100]])
# # 用仿射变换实现平移
# img_s = cv2.warpAffine(img, M, (cols, rows), borderValue=(155, 150, 200))
#
# cv2.imshow('img_s', img_s)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 旋转
# img = cv2.imread('car.jpg', 0)
#
# rows, cols = img.shape
#
# M = cv2.getRotationMatrix2D((cols / 2, rows / 2,), 45, 0.6)  # 旋转中心，旋转角度，旋转后的缩放因子
#
# # 第三个参数是输出图像的尺寸中心
# dst = cv2.warpAffine(img, M, (2 * cols, 2 * rows))
#
# while 1:
#     cv2.imshow('img', dst)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()


# 仿射变换
# rows, cols, ch = img.shape
#
# pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
# pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.2], [cols * 0.1, rows * 0.9]])
#
# M = cv2.getAffineTransform(pts1, pts2)
#
# dst = cv2.warpAffine(img, M, (cols, rows))
#
# cv2.imshow('image', dst)
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()


# 透视变换
# 选四个点且任意三个不能共线
# getPerspectiveTransform()
#
# warpPerspective()
