import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)  # 创建一个黑色图像

# 画线
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)  # 图像，起点，终点，蓝色，线宽5px
# 画矩形 需要指定左上角顶点和右下角顶点
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# 画圆 需要指定圆心和半径
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
# 画椭圆 需要中心坐标、长轴、短轴、沿逆时针旋转的角度、沿顺时针方向起始的角度和结束角度
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# 画多边形 需要指定每个顶点的坐标
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的;
# 如果第三个参数是 False，我们得到的多边形是不闭合的
pts = pts.reshape(-1, 1, 2)
cv2.polylines(img, pts=[pts], isClosed=True, color=(0, 0, 255), thickness=3)
# 在图上添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
