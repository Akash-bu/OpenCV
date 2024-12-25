import cv2 as cv

img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\group 1.jpg')
cv.imshow('group', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('har_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'faces = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('det face', img)


cv.waitKey(0)