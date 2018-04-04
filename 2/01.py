# -*- coding=GBK -*-
import cv2 as cv


# 显示图片
src = cv.imread("1.jpg")
cv.namedWindow("哈", cv.WINDOW_NORMAL)   # 可以调节大小，去掉此行代码不能调节大小
cv.imshow("哈", src)
cv.waitKey()
cv.destroyAllWindows()
