import cv2 as cv
import numpy as np

img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\park.jpg')
cv.imshow('cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#laplacion

lap = cv.Laplacian(gray, cv.CV_64F)

lap = np.uint8(np.absolute(lap))
cv.imshow('lap', lap)

#sobel


sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('sobel x', sobelx)
cv.imshow('sobel y', sobely)

sobel_comb = cv.bitwise_or(sobelx, sobely)
cv.imshow('comb', sobel_comb)

canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)

cv.waitKey(0)