import cv2 as cv

img = cv.imread('D:\openCV tut\opencv-course\Resources\Photos\cat.jpg')

#cv.imshow('cat', img)

# cv.waitKey(0)
# cv.destroyAllWindows()

def rescale(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale) 

    dim = (width, height)


    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(0)

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

changeRes(640,480)

# capture = cv.VideoCapture('D:\openCV tut\opencv-course\Resources\Videos\kitten.mp4')




while True:
    isTrue, frame = capture.read()

    # frame_resized = rescale(frame, scale = 0.25)

    # frame_resized = changeRes(640,480)

    #cv.imshow('Video', frame)
    cv.imshow('Video resized', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# resized_img = rescale(img)

# cv.imshow('cat resized', resized_img)
cv.waitKey(0)
capture.release()
cv.destroyAllWindows()