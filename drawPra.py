import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")

# cv.imshow("blank", blank)

# blank[200:300, 300:400] = 0,255,0

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)

#line

cv.line(blank, (100,250),(300,400), (255,255,255), thickness=3 )


#text

text = cv.putText(blank, 'hello', (225,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

cv.imshow("green screen", text)
cv.waitKey(0)
cv.destroyAllWindows()