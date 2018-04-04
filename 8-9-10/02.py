# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# ��ȡͼƬ�е�ָ���������ָ���������ĳһͼƬ
def jie_image(src1):
    src2 = src1[5:89, 500:630]  # ��ȡ��5�е�89�еĵ�500�е�630�е�����
    cv.imshow("��ȡ", src2)
    src1[105:189, 300:430] = src2   # ָ��λ����䣬��СҪһ���������
    cv.imshow("�ϳ�", src1)


# ָ����ɫ���
def fill_image(image):
    copyImage = image.copy()    # ����ԭͼ��
    h, w = image.shape[:2]  # ��ȡͼ��Ŀ�͸�
    # mask = np.zeros([h+2, w+2], np.uint8)# �½�ͼ�����  +2�ǹٷ�����Ҫ��
    # cv.floodFill(copyImage, mask, (0, 80), (0, 100, 255), (100, 100, 50), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    # cv.imshow("���", copyImage)

    mask = np.ones([h+2, w+2, 1], np.uint8) # �½�ͼ�����  +2�ǹٷ�����Ҫ��
    mask[200:300, 200:300] = 0
    cv.floodFill(copyImage, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("���2", copyImage)


#ָ��λ�����
def fill2_image():
    image = np.zeros([200, 200, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow("ԭͼ", image)
    mask = np.ones([202, 202, 1], np.uint8)
    mask[100:150, 100:150] = 0
    cv.floodFill(image, mask, (100, 100), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("���2", image)

# src = cv.imread("1.jpg")
# cv.imshow("ԭ��", src)
fill2_image()
cv.waitKey(0)
cv.destroyAllWindows()
