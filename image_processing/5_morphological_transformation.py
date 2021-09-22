import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('car.jpg', 0)

kernel = np.ones((5, 5), np.uint8)

# 形态学转换
plt.subplot(3, 3, 1)
plt.imshow(img, 'gray')
plt.title('original')
plt.xticks([]), plt.yticks([])
# 腐蚀（前景物体会变小，整幅图像的白色区域会减少。这对于去除白噪声很有用，也可以用来断开两个连在一块的物体等。）
erosion = cv2.erode(img, kernel, iterations=1)
plt.subplot(3, 3, 2)
plt.imshow(erosion, 'gray')
plt.title('erosion')
plt.xticks([]), plt.yticks([])

# 膨胀（增加图像中的白色区域（前景），也可以用来连接两个分开的物体）
dilation = cv2.dilate(img, kernel, iterations=1)
plt.subplot(3, 3, 3)
plt.imshow(dilation, 'gray')
plt.title('dilation')
plt.xticks([]), plt.yticks([])

# 开运算（先腐蚀再进行膨胀就叫做开运算，用来去除噪声）
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
plt.subplot(3, 3, 4)
plt.imshow(opening, 'gray')
plt.title('opening')
plt.xticks([]), plt.yticks([])

# 闭运算（先膨胀再腐蚀。它经常被用来填充前景物体中的小洞，或者前景物体上的小黑点）
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.subplot(3, 3, 5)
plt.imshow(closing, 'gray')
plt.title('closing')
plt.xticks([]), plt.yticks([])

# 形态学梯度（其实就是一幅图像膨胀与腐蚀的差别。结果看上去就像前景物体的轮廓）
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.subplot(3, 3, 6)
plt.imshow(gradient, 'gray')
plt.title('gradient')
plt.xticks([]), plt.yticks([])

# 礼帽（原始图像与进行开运算之后得到的图像的差）
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
plt.subplot(3, 3, 7)
plt.imshow(tophat, 'gray')
plt.title('tophat')
plt.xticks([]), plt.yticks([])

# 黑帽（进行闭运算之后得到的图像与原始图像的差）
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
plt.subplot(3, 3, 8)
plt.imshow(blackhat, 'gray')
plt.title('blackhat')
plt.xticks([]), plt.yticks([])

plt.show()
