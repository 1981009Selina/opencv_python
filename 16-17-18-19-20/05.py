# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


#轮廓发现
def contous_image(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("二值化", binary)
    cloneImage, contous, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i,contou in enumerate(contous):
        cv.drawContours(image, contous, i, (0, 0, 255), 1)
    cv.imshow("轮廓", image)
    for i,contou in enumerate(contous):
        cv.drawContours(image, contous, i, (0, 0, 255), -1)
    cv.imshow("轮廓覆盖", image)


src = cv.imread("02.png")
cv.imshow("原来", src)
contous_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
