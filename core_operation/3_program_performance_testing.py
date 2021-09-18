import timeit

# 用窗口大小不同（ 5， 7， 9）的核函数来做中值滤波
# img1 = cv2.imread('car.jpg')
#
# e1 = cv2.getTickCount()
# for i in range(5, 49, 2):
#     img1 = cv2.medianBlur(img1, i)
# e2 = cv2.getTickCount()
# # 得到函数运行了多少秒
# t = (e2 - e1) / cv2.getTickFrequency()
# print(t)


# # 查看优化是否被开启（默认开启）
# print('before:', cv2.useOptimized())
# # 开启优化
# cv2.setUseOptimized(False)
# print('after:', cv2.useOptimized())


# timeit会让程序运行几次以得到一个准确的结果
print(timeit.timeit('y = 5 * 5'))
print(timeit.timeit('y = 5 ** 2'))
# 一般情况下opencv的函数比numpy的函数快
