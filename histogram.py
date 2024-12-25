import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#histogram for a grayscale image

img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\cats.jpg')
cv.imshow('cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

'''

calculates the center coordinates of an image in terms of its width and height. Here's how it works:

img.shape[1]: Represents the width of the image (number of columns).
img.shape[0]: Represents the height of the image (number of rows).
// 2: Performs integer division by 2, effectively finding the midpoint.
'''

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('circle', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('mask', masked)

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

# plt.figure()
# plt.title('Grayscale hist')
# plt.xlabel('Bins')
# plt.ylabel("# pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#color histogram


plt.figure()
plt.title('color hist')
plt.xlabel('Bins')
plt.ylabel("# pixels")
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, 256, [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)
