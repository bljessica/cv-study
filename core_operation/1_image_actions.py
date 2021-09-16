import cv2
from matplotlib import pyplot as plt

img = cv2.imread('car.jpg')
px = img[100, 100]  # 根据图像的行列坐标获取像素值(B, G, R)
print(px)
blue = img[100, 100, 0]  # 行列坐标, B
print(blue)
# 可以以类似的方式修改像素值
img[100, 100] = [255, 255, 255]
print(img[100, 100])
# Numpy 是经过优化了的进行快速矩阵运算的软件包。所以不推荐
# 逐个获取像素值并修改，这样会很慢，能有矩阵运算就不要用循环


# 上面提到的方法被用来选取矩阵的一个区域，比如说前 5 行的后 3列。
# 对于获取每一个像素值，用 Numpy 的 array.item() 和 array.itemset() 会更好。但是返回值是标量。
# 如果想获得所有 B， G， R 的值，你需要使用 array.item() 分割他们。
print('item:')
print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))
print('shape:', img.shape)  # 行，列，通道数
print('size:', img.size)  # 像素数
print('data type:', img.dtype)  # 数据类型

# 图像ROI（region of interest）
# tmp = img[120:170, 110:160]
# img[120:170, 50:100] = tmp
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 拆分及合并通道
# b, g, r = cv2.split(img)
# img = cv2.merge([b, g, r])
# b = img[:, :, 0]  # 取图片某通道的值
# img[:, :, 2] = 0  # 让红色通道值都为0
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 为图像扩边（填充）
BLUE = [255, 0, 0]

replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT)

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()
