import cv2
import numpy as np 
x=cv2.imread("c:/users/girishhegde/dog.jpg")
cv2.imshow("dog",x)
y=cv2.cvtColor(x,cv2.COLOR_BGR2Lab)
cv2.imshow("lab",y[:,:,0])
cv2.waitKey(0)