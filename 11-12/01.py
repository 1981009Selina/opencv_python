# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


def mo_image(src1):
    src2 = cv.blur(src1, (5, 5))
    cv.imshow("��ֵģ��", src2)

    src2 = cv.medianBlur(src1, 5)
    cv.imshow("��ֵģ��", src2)

    src2 = cv.GaussianBlur(src1, (5, 5), 2)
    cv.imshow("��˹ģ��", src2)

    src2 = cv.bilateralFilter(src1, 5, 5, 2)
    cv.imshow("˫���˲�", src2)


# �Զ���ģ������
def zi_image(src1):
    kernel1 = np.ones((5, 5), np.float)/25  # �Զ�����󣬲���ֹ��ֵ���
    src2 = cv.filter2D(src1, -1, kernel1)
    cv.imshow("�Զ����ֵģ��", src2)
    kernel2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    src2 = cv.filter2D(src1, -1, kernel2)
    cv.imshow("�Զ�����", src2)

src = cv.imread("1.jpg")
cv.namedWindow("ԭ��", cv.WINDOW_NORMAL)
cv.imshow("ԭ��", src)
zi_image(src)
mo_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
