import cv2
import numpy as np

# flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flags)
# 在 OpenCV 的 HSV 格式中， H（色彩/色度）的取值范围是 [0， 179]，S（饱和度）的取值范围 [0， 255]， V（亮度）的取值范围 [0， 255]。
# 但是不同的软件使用的值可能不同。所以当你需要拿 OpenCV 的 HSV 值与其他软件的 HSV 值进行对比时，一定要记得归一化。


# 物体跟踪
# 在 HSV 颜色空间中要比在 BGR 空间中更容易表示一个特定颜色。
cap = cv2.VideoCapture(0)

# 找到蓝色的HSV值
# blue = np.uint8([[[255, 0, 0]]])
# hsv_blue = cv2.cvtColor(blue, cv2.COLOR_RGB2HSV)
# print(hsv_blue)

while 1:
    # 获取每一帧
    ret, frame = cap.read()

    # 转换到HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 设定蓝色的阈值
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # 根据阈值构建掩膜
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 对原图像和掩膜进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
