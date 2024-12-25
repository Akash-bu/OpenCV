import cv2 as cv

img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\park.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("gray image", gray)


blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT )


#canny edge

canny = cv.Canny(blur, 125, 175)

canny_edge = cv.imshow("canny", canny)


#dilte image


dilate = cv.dilate(canny, (3,3), iterations=2)

dil_img = cv.imshow("dil", dilate)

#erode

eroded = cv.erode(dilate, (3,3), iterations=2)
erod = cv.imshow("eroded_img", eroded)

#resize

resized = cv.resize(img, (300,300), interpolation=cv.INTER_CUBIC)
resize = cv.imshow("resized", resized)

#cropping

crop = img[100:200, 150:300]
cropped = cv.imshow("crop", crop)

cv.imshow("blur", blur)
cv.waitKey(0)