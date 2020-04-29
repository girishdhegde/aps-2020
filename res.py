import cv2
import numpy as np 


x=cv2.imread("c:/users/girishhegde/m23.png")
y=cv2.resize(x,(186,271),interpolation=cv2.INTER_AREA)
cv2.imwrite("downloadhalf4.jpg",y)