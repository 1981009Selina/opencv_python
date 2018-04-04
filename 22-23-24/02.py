# -*- coding=GBK -*-
import cv2 as cv


# �������
def face_image():
  gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
  face_detector = cv.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")
  faces = face_detector.detectMultiScale(gray, 1.02, 5)   # �ڶ����������ƶ����룬������������ʶ��ȣ�Խ��ʶ���Խ��
  for x, y, w, h in faces:
    cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 2)   # ������������һ������ɫ��һ���Ǳ߿���
  cv.imshow("���", src)


src = cv.imread("4.jpg")
cv.imshow("ԭ��", src)
face_image()
cv.waitKey(0)
cv.destroyAllWindows()
