import cv2 as cv
import numpy as np
img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\cats.jpg')
cv.imshow('cats', img)

#simple thresholding

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#100 is the max value, anything below this is made black and above this is made white

threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('thres', thresh)
print(threshold)

threshold_inv, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('thres inv', thresh_inv)
print(threshold_inv)

#adaptive thresholding

adap = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('adap', adap)



cv.waitKey(0)
