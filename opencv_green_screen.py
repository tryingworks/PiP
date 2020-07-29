import cv2
import numpy as np

W=320
H=240
cap = cv2.VideoCapture(0)
cap.set(3, W)
cap.set(4, H)
kernel = np.ones((5,5),np.uint8)
mask1 = np.empty((H,W),dtype=np.uint8)
mask2 = np.empty((H,W),dtype=np.uint8)
mask = np.empty((H,W),dtype=np.uint8)

hsv = np.zeros((H,W,3), dtype=np.uint8)
np.set_printoptions(precision=2)
while True:

    ret, frame = cap.read()
    cv2.cvtColor(frame, cv2.COLOR_BGR2HSV,dst=hsv)
    np.less(hsv[:,:,0],40 ,out=mask1)
    np.greater(hsv[:,:,0],90,out=mask2)
    np.logical_or(mask1,mask2,out=mask1)

    np.less(hsv[:,:,2],90,out=mask2)
    np.logical_or(mask1,mask2,out=mask1)

    np.less(hsv[:,:,1],50, out=mask2)
    np.logical_or(mask1,mask2,out=mask1)

    cv2.imshow("video2", np.fliplr(frame*mask1[:,:,None]))
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()