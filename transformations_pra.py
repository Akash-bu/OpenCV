import cv2 as cv
import numpy as np

img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\park.jpg')

# cv.imshow('Park', img)

#translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat,dim)

#x right
#-x left
#y down
#-y up

translated = translate(img, -100, -100)
cv.imshow("translated", translated)


#rotate

def rotate(img, angle, rotpoint = None):
    (height, width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dim = (width, height)

    return cv.warpAffine(img, rotMat, dim)


rotated = rotate(img, -45)

cv.imshow("rotated_image",rotated)

rotated_2 = rotate(rotated, -90)

cv.imshow("rotated_image_2",rotated_2)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)

cv.imshow("resized", resized)

#flip

flip = cv.flip(img, -1)
cv.imshow("flipped", flip)

#crop

cropped = img[200:300, 400:500]
cv.imshow("cropped", cropped)

cv.waitKey(0)