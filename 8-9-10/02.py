# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# 截取图片中的指定区域或在指定区域添加某一图片
def jie_image(src1):
    src2 = src1[5:89, 500:630]  # 截取第5行到89行的第500列到630列的区域
    cv.imshow("截取", src2)
    src1[105:189, 300:430] = src2   # 指定位置填充，大小要一样才能填充
    cv.imshow("合成", src1)


# 指定颜色填充
def fill_image(image):
    copyImage = image.copy()    # 复制原图像
    h, w = image.shape[:2]  # 读取图像的宽和高
    # mask = np.zeros([h+2, w+2], np.uint8)# 新建图像矩阵  +2是官方函数要求
    # cv.floodFill(copyImage, mask, (0, 80), (0, 100, 255), (100, 100, 50), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    # cv.imshow("填充", copyImage)

    mask = np.ones([h+2, w+2, 1], np.uint8) # 新建图像矩阵  +2是官方函数要求
    mask[200:300, 200:300] = 0
    cv.floodFill(copyImage, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("填充2", copyImage)


#指定位置填充
def fill2_image():
    image = np.zeros([200, 200, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow("原图", image)
    mask = np.ones([202, 202, 1], np.uint8)
    mask[100:150, 100:150] = 0
    cv.floodFill(image, mask, (100, 100), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("填充2", image)

# src = cv.imread("1.jpg")
# cv.imshow("原来", src)
fill2_image()
cv.waitKey(0)
cv.destroyAllWindows()
