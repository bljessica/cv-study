import cv2

# 用窗口大小不同（ 5， 7， 9）的核函数来做中值滤波
img1 = cv2.imread('car.jpg')

e1 = cv2.getTickCount()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickFrequency()
print(t)
