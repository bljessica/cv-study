import cv2
import numpy as np

# 图像加法
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y), x + y)

# 图像混合
# img1 = cv2.imread('car.jpg')
# img1 = img1[:167, :274, :]
# img2 = cv2.imread('cat.jpg')
# img2 = img2[:167, :274, :]
# # 将图像size转为相同才能混合
# print(img1.size, img1.shape, img2.size, img2.shape)
#
# dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
#
# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 按位运算
img1 = cv2.imread('car.jpg')
img1 = img1[:167, :274, :]
img2 = cv2.imread('cat.jpg')
img2 = img2[:167, :274, :]

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 168, 275, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 取 roi 中与 mask 中不为零的值对应的像素的值，其他值为 0
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
img2_bg = cv2.bitwise_and(img2, img2, mask=mask_inv)

dst = cv2.add(img1_bg, img2_bg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
