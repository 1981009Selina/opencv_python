# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# ��Ƶ����ĳһ��ɫ
def nextrace_object_demo():
    capture = cv.VideoCapture("1.mp4")
    while True:
        ret, frame = capture.redad()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # ת��ɫ�ʿռ�Ϊhsv
        # ���ð�ɫ�ķ�Χ��������Ƶ�еİ�ɫ
        lower_hsv = np.array([0, 0, 221])   # ���ù��˵���ɫ�ĵ�ֵ
        upper_hsv = np.array([180, 30, 255])    # ���ù��˵���ɫ�ĸ�ֵ
        mask = cv.inRange(hsv, lower_hsv, upper_hsv)    # ����ͼ����ɫ��Ϣ��H�������Ͷȣ�S�������ȣ�V�����䣬ѡ���ɫ����
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        if cv.waitKey(50) & 0xFF == ord('q'):
            break

# src = cv.imread("1.jpg")
# cv.namedWindow("ԭ��", cv.WINDOW_NORMAL)
# cv.imshow("ԭ��", src)
# t1 = cv.getTickCount()
#
nextrace_object_demo()
# t2 = cv.getTickCount()
# time = (t2 - t1)*1000/cv.getTickFrequency()
# print("time: %s" % time)
cv.waitKey(0)
cv.destroyAllWindows()
