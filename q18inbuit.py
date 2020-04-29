import cv2
import numpy as np
import random

img = cv2.imread('house.tif', 0)


cv2.imshow('img', img)


l=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('laplacian', ls)
hz=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
cv2.imshow('hwith', hz)
vz=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
cv2.imshow('vwith', vz)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()



