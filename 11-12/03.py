# -*- coding=GBK -*-
import cv2 as cv
# from matplotlib import pyplot as plt

import  matplotlib.pyplot as plt

#提升对比度（默认提升），只能是灰度图像
def equalHist_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("原   来", gray)
    dst = cv.equalizeHist(gray)
    cv.imshow("默认处理", dst)


#对比度限制（自定义提示参数）
def clahe_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))
    dst = clahe.apply(gray)
    cv.imshow("自定义处理", dst)

src = cv.imread("1.jpg")
equalHist_image(src)
clahe_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
