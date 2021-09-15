import cv2

vc = cv2.VideoCapture('plane.mp4')

# 检查是否打开正确
if vc.isOpened():
    isOpen, frame = vc.read()  # frame是当前帧的图像
else:
    isOpen = False

while open:
    ret, frame = vc.read()
    if frame is None:  # 图像为空
        break
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将图像转为灰度图像
        cv2.imshow('result', gray)
        if cv2.waitKey(10) & 0xFF == 27:  # 按esc退出（如果waitKey时间太短会出不来，太长播放会很慢）
            break

vc.release()
cv2.destroyAllWindows()
