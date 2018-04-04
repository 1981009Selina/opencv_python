# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# 粗略的调节对比度和亮度
def contrast_brightness_image(src1, a, g):
    h, w, ch = src1.shape   # 获取shape的数值，height和width、通道

    # 新建全零图片数组src2,将height和width，类型设置为原图片的通道类型(色素全为零，输出为全黑图片)
    src2 = np.zeros([h, w, ch], src1.dtype)
    dst = cv.addWeighted(src1, a, src2, 1-a, g) # addWeighted函数说明如下
    cv.namedWindow("修改后", cv.WINDOW_NORMAL)
    cv.imshow("修改后", dst)

src = cv.imread("1.jpg")
cv.namedWindow("原来", cv.WINDOW_NORMAL)
cv.imshow("原来", src)
contrast_brightness_image(src, 1.2, 0)  # 第一个1.2为对比度  第二个为亮度
cv.waitKey(0)
cv.destroyAllWindows()
