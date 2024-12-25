import cv2 as cv
import numpy as np

img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\park.jpg')
cv.imshow('boston park', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

#img.shape[:2]: Extracts the height and width of the image (the first two dimensions of the img array). For an image with shape (427, 640, 3), img.shape[:2] would be (427, 640).

#np.zeros((427, 640), dtype='uint8'): Creates a blank (black) 2D array of size (427, 640) filled with zeros. The dtype='uint8' ensures the data type of the array elements is unsigned 8-bit integers (values range from 0 to 255, suitable for image data).

b1,g,r = cv.split(img)

blue = cv.merge([b1, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])



cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

print(img.shape)
print(b1.shape)
print(g.shape)
print(r.shape)

#merge

merged = cv.merge([b1,g,r])
cv.imshow('Merged image', merged)

cv.waitKey(0)