import  cv2
import numpy as np

def circle_shape(event,x,y,flagval,var):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image_window,(x,y),50,(255,0,0),-1)

cv2.namedWindow(winname='image_window')
cv2.setMouseCallback('image_window',circle_shape)

image_window=np.zeros((1024,1024,3),np.uint8)

while True:
    cv2.imshow('image_window',image_window)

    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()