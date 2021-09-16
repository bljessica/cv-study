import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)


# 在双击的地方画一个圆
# def draw_circle_on_double_click(event, x, y, flag, param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
#
#
# # 创建图像与窗口并将窗口与回调函数绑定
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle_on_double_click)
#
# while 1:
#     cv2.imshow('image', img)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()


# 根据选择的模式在拖动鼠标时绘制矩形或者是圆圈
drawing = False
mode = True # 画矩形/圆
ix, iy = -1, -1


def draw_circle_or_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:  # 绘制圆，圆连在一起就成了线
                cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


img = np.zeros([512, 512, 3], np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle_or_rectangle)
while 1:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('q'):
        break
