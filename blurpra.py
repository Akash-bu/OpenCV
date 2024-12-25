import cv2 as cv

img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\cats.jpg')
cv.imshow('cats', img)

#smoothing
#averaging

average = cv.blur(img, (7,7))
cv.imshow("avg blur", average)

#guassian blur

guass = cv.GaussianBlur(img, (7,7), 2)
cv.imshow("guass blur img", guass)

#median blur

median = cv.medianBlur(img, 7)
cv.imshow('median', median)

#bilateral blur

bilateral = cv.bilateralFilter(img, 10, 40, 30)
cv.imshow("bilateral", bilateral)


cv.waitKey(0)