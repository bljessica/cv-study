import cv2

# opencv 读取的格式是BGR
img = cv2.imread('car.jpg')
# car_img = img[0:100, 0:100]  # 截取部分图像

# img_gray = cv2.imread('car.jpg', cv2.IMREAD_GRAYSCALE)  # 读取灰度图像
# print(img, img.shape)  # [h, w, c]


cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # 窗口可以调整大小
cv2.imshow('image', img)
k = cv2.waitKey(0)  # 任意键
if k == 27:  # 按esc退出
    cv2.destroyAllWindows()
elif k == ord('s'):  # 按s保存退出
    cv2.imwrite('my_car.png', img)
    cv2.destroyAllWindows()


# print(type(img), img.size, img.dtype)
