# -*- coding=GBK -*-
import cv2 as cv
from matplotlib import pyplot as plt


#����ͼ���ֱ��ͼ
def hist_image(image):
    color = ("blue", "green", "red")
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()

src = cv.imread("1.jpg")
cv.namedWindow("ԭ��", cv.WINDOW_NORMAL)
cv.imshow("ԭ��", src)
hist_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
