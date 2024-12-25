import cv2 as cv
import numpy as np
img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\cats.jpg')

cv.imshow("catty", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("blurry",blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow("canny", canny)

#binarize am image
ret, threshold = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thres', threshold)

contours, hierarchies = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contours found!')


#draw the edges
blc = cv.drawContours(blank, contours, -1, (0,255,0), 2)
cv.imshow("cont drawn", blc)



cv.waitKey(0)