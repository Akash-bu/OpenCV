import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\park.jpg')

cv.imshow('park',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray image", gray)


hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv img', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab', lab)

# plt.imshow(img)
# plt.show()

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

hsv2bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv2bgr', hsv2bgr)

lab2bgr = cv.cvtColor(lab, cv.COLOR_Lab2BGR)
cv.imshow('lab2bgr', hsv2bgr)

rgb2bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow('rgb2bgr',rgb2bgr)




cv.waitKey(0)