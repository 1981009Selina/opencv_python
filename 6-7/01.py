# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# 视频跟踪某一颜色
def nextrace_object_demo():
    capture = cv.VideoCapture("1.mp4")
    while True:
        ret, frame = capture.redad()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # 转换色彩空间为hsv
        # 设置白色的范围，跟踪视频中的白色
        lower_hsv = np.array([0, 0, 221])   # 设置过滤的颜色的低值
        upper_hsv = np.array([180, 30, 255])    # 设置过滤的颜色的高值
        mask = cv.inRange(hsv, lower_hsv, upper_hsv)    # 调节图像颜色信息（H）、饱和度（S）、亮度（V）区间，选择白色区域
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        if cv.waitKey(50) & 0xFF == ord('q'):
            break

# src = cv.imread("1.jpg")
# cv.namedWindow("原来", cv.WINDOW_NORMAL)
# cv.imshow("原来", src)
# t1 = cv.getTickCount()
#
nextrace_object_demo()
# t2 = cv.getTickCount()
# time = (t2 - t1)*1000/cv.getTickFrequency()
# print("time: %s" % time)
cv.waitKey(0)
cv.destroyAllWindows()
