import cv2
import matplotlib.pyplot as plt
import numpy as np

# opencv 读取的格式是BGR
img = cv2.imread('car.jpg')
img_gray = cv2.imread('car.jpg', cv2.IMREAD_GRAYSCALE)
# print(img, img.shape)  # [h, w, c]


def cv2_show(image):
    cv2.imshow('img', image)
    cv2.waitKey(0)  # 任意键终止
    cv2.destroyAllWindows()


cv2_show(img)
cv2_show(img_gray)

# 保存
# cv2.imwrite('my_car.png', img)

print(type(img), img.size, img.dtype)