# -*- coding=GBK -*-
import cv2 as cv


# ��ʾͼƬ
src = cv.imread("1.jpg")
cv.namedWindow("��", cv.WINDOW_NORMAL)   # ���Ե��ڴ�С��ȥ�����д��벻�ܵ��ڴ�С
cv.imshow("��", src)
cv.waitKey()
cv.destroyAllWindows()
