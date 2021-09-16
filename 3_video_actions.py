import cv2

cap = cv2.VideoCapture('plane.mp4')  # 参数为0则打开电脑摄像头
# print(cap.get(3), cap.get(4))  # 查看每一帧的宽和高(580, 362)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter('my_plane.avi', fourcc, 20.0, (width, height))


while cap.isOpened():
    ret, frame = cap.read()  # 一帧一帧地捕获视频
    if frame is None:  # 图像为空
        break
    if ret:
        # 播放
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将图像转为灰度图像
        # cv2.imshow('result', gray)
        # if cv2.waitKey(25) & 0xFF == ord('q'):  # 按q退出（如果waitKey时间太短会播放太快，太长会播放很慢）
        #     break
        # 从摄像头中捕获视频，沿水平方向旋转每一帧并保存它
        frame = cv2.flip(frame, 0)
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break

# 停止捕获
cap.release()
out.release()
cv2.destroyAllWindows()
