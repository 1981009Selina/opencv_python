# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# numpy数组操作
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
    cv.imshow("修改后", image)


def create_image():
    img = np.zeros([400, 400, 3], np.uint8) # zeros:double类零矩阵  创建400*400 3个通道的矩阵图像 参数时classname为uint8
    img[:, :, 0] = np.ones([400, 400])*255  # ones([400, 400])是创建一个400*400的全1矩阵，*255即是全255矩阵 并将这个矩阵的值赋给img的第一维
    img[:, :, 1] = np.ones([400, 400])*255  # 第二维全是255
    img[:, :, 2] = np.ones([400, 400])*255  # 第三维全是255
    cv.imshow("自制图片", img)  # 输出一张400*400的白色图片(255 255 255):蓝(B)、绿(G)、红(R)


def create_image2():
    img = np.ones([400, 400, 1], np.uint8)
    img = img * 127
    cv.imshow("自制图片", img)  # 输出一张400*400的白色图片(255 255 255):蓝(B)、绿(G)、红(R)

#src = cv.imread("1.jpg")
#cv.namedWindow("原来", cv.WINDOW_NORMAL)
# cv.imshow("原来", src)
# t1 = cv.getTickCount()#毫秒级别的计时函数,记录了系统启动以来的时间毫秒
# access_pixles(src)
# t2 = cv.getTickCount()
# time = (t2 - t1)*1000/cv.getTickFrequency()#getTickFrequency用于返回CPU的频率,就是每秒的计时周期数
# print("time: %s" % time)
create_image2()
cv.waitKey(0)
cv.destroyAllWindows()


