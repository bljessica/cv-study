import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('car.jpg', 0)

# 梯度滤波器（高通滤波器）：Sobel, Scharr, Laplacian
# cv2.CV_64F 输出图像的深度（数据类型），可以使用-1, 与原图像保持一致
laplacian = cv2.Laplacian(img, cv2.CV_64F)
# 参数 1,0 为只在 x 方向求一阶导数，最大可以求 2 阶导数
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# 参数 0,1 为只在 y 方向求一阶导数，最大可以求 2 阶导数
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()

# 我们可以通过参数 -1 来设定输出图像的深度（数据类型）与原图像保持一致，但是我们在代码中使用的却是 cv2.CV_64F。这是为什么呢？
# 想象一下一个从黑到白的边界的导数是整数，而一个从白到黑的边界点导数却是负数。
# 如果原图像的深度是np.int8 时，所有的负值都会被截断变成 0，换句话说就是把把边界丢失掉。
# 所以如果这两种边界你都想检测到，最好的的办法就是将输出的数据类型设置的更高，比如 cv2.CV_16S， cv2.CV_64F 等。取绝对值然后再把它转回
# 到 cv2.CV_8U。
