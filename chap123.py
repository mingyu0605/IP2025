import numpy as np
import cv2
# Create a black image
# img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('dog.jpg')
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
img = cv2.rectangle(img(384,0),(510,128),(0,255,0),3)
img = cv2.circle(img(447,63), 63, (0,0.255),30)
img = cv2.ellipse(img(256,256),(100,50),0,0,180,255,-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 8,(255,255,255),12,cv2.LINE_AA)
cv2.imshow('frame',img)
k = cv2.waitKey(0)
if k == 27: # wait for 's' key to save and exit
    cv2.destroyAllWindows()