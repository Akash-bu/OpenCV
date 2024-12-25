import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (350,350), 255, -1)
rectangle2 = cv.rectangle(blank.copy(), (30,30), (380,380), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)


cv.imshow('rect', rectangle)
cv.imshow('circle', circle)

#intersection
band = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwiseand', band)

#union
bor = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwiseor', bor)

#non intersection
bxor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitxor', bxor)

#not

bnot = cv.bitwise_not(circle)
cv.imshow('bitxnot', bnot)

cv.waitKey(0)