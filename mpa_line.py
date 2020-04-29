import cv2
import numpy as np 



img=np.zeros((500,500),np.uint8)
#cv2.imshow("img",img)

xl=500
yl=500

x1=0
y1=0
x2=325
y2=400


dx=x2-x1
dy=y2-y1

m=dy/dx

for i in range(x1,x2):
	img[i,j]=255
	y=y+m


cv2.imshow("dda",img)



