import cv2
import numpy as np

draw=False
ix,iy=-1,-1

def rectangle_shape(event,x,y,flagval,par):
    global draw,ix,iy

    if event == cv2.EVENT_LBUTTONDOWN:
        draw=True
        ix,iy=x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        draw=False
        cv2.rectangle(image_window,(ix,iy),(x,y),(255,0,0),-1)

image_window=np.zeros((1024,1024,3),np.uint8)

cv2.namedWindow(winname='Image_Window')
cv2.setMouseCallback('Image_Window',rectangle_shape)

while True:
    cv2.imshow('Image_Window',image_window)

    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()