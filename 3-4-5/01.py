# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# ���ͼƬ����
def get_image_info(image):  # ����һ�����������ͼƬ��һЩ����
    print(type(image))  # ��ʾͼƬ���� numpy���͵�����
# ͼ������shape���Ա�ʾͼ��Ĵ�С��shape�᷵��tupleԪ�飬��һ��Ԫ�ر�ʾ�����������ڶ���Ԫ���ʾ����������������Ԫ����3����ʾ����ֵ�ɹ����ԭɫ���
    print(image.shape)
    print(image.size)   # ͼ���С
    print(image.dtype)  # ͼ������
    pixel_data = np.array(image)
    print(pixel_data)   # ͼƬ����


src = cv.imread("1.jpg")
cv.namedWindow("��", cv.WINDOW_NORMAL)
cv.imshow("��", src)
get_image_info(src)
cv.imwrite("2.png", src)    # ͼƬ���Ϊ����Ҫ�浽c�̣�ҪȨ�޵�
cv.waitKey(0)
cv.destroyAllWindows()
