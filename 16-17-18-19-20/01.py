# -*- coding=GBK -*-
import cv2 as cv


#ͼ���ݶȣ�����������
def sobel_image(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)#x������
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)#y������
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("X����", gradx)#��ɫ�仯��ˮƽ�ֲ�
    cv.imshow("Y����", grady)#��ɫ�仯�ڴ�ֱ�ֲ�
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("�ϳ�", gradxy)


#ͼ���ݶȣ�scharr����,��ǿ��Ե
def scharr_image(image):
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)#x������
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)#y������
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("X����", gradx)#��ɫ�仯��ˮƽ�ֲ�
    cv.imshow("Y����", grady)#��ɫ�仯�ڴ�ֱ�ֲ�
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("�ϳ�", gradxy)


#������˹����
def lapalian_image(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("������˹", lpls)

src = cv.imread("1.jpg")
cv.imshow("ԭ��", src)
lapalian_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
