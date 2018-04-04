# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# numpy�������
def access_pixles(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    print("width : %s, height : %s, channel : %s" % (width, height, channel))
    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("�޸ĺ�", image)


def create_image():
    img = np.zeros([400, 400, 3], np.uint8) # zeros:double�������  ����400*400 3��ͨ���ľ���ͼ�� ����ʱclassnameΪuint8
    img[:, :, 0] = np.ones([400, 400])*255  # ones([400, 400])�Ǵ���һ��400*400��ȫ1����*255����ȫ255���� ������������ֵ����img�ĵ�һά
    img[:, :, 1] = np.ones([400, 400])*255  # �ڶ�άȫ��255
    img[:, :, 2] = np.ones([400, 400])*255  # ����άȫ��255
    cv.imshow("����ͼƬ", img)  # ���һ��400*400�İ�ɫͼƬ(255 255 255):��(B)����(G)����(R)


def create_image2():
    img = np.ones([400, 400, 1], np.uint8)
    img = img * 127
    cv.imshow("����ͼƬ", img)  # ���һ��400*400�İ�ɫͼƬ(255 255 255):��(B)����(G)����(R)

#src = cv.imread("1.jpg")
#cv.namedWindow("ԭ��", cv.WINDOW_NORMAL)
# cv.imshow("ԭ��", src)
# t1 = cv.getTickCount()#���뼶��ļ�ʱ����,��¼��ϵͳ����������ʱ�����
# access_pixles(src)
# t2 = cv.getTickCount()
# time = (t2 - t1)*1000/cv.getTickFrequency()#getTickFrequency���ڷ���CPU��Ƶ��,����ÿ��ļ�ʱ������
# print("time: %s" % time)
create_image2()
cv.waitKey(0)
cv.destroyAllWindows()


