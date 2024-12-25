import cv2 as cv
import numpy as np
img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\cats 2.jpg')
cv.imshow('cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#define a circular mask
mask = cv.circle(blank, (img.shape[1]//2 + 60, img.shape[0]//2), 100, 255, -1)
cv.imshow('masked', mask)

#use circular mask on a image 
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('maskedbitwise', masked)



cv.waitKey(0)