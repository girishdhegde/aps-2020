import cv2
import numpy as np 
import math


img=np.zeros((500,500),np.uint8)
#cv2.imshow("img",img)
xl=500-1
yl=500-1

x1=50
y1=50

x2=100
y2=200


m=(y2-y1)/(x2-x1)

t=math.atan(m)*180/np.pi

print("angle=",t)

if t>45:

	h=x1
	x1=y1
	y1=h
	k=x2
	x2=y2
	y2=k


dx=x2-x1
dy=y2-y1

x=x1
y=y1

img[yl-y,x]=255

d=dy-(dx/2)

for x in range(x1+1,x2):

	if d<0:
		d=d+dy
	else:
		d=d+dy-dx
		y=y+1
	if t>45:
		img[yl-x,y]=255
	else:
		img[yl-y,x]=255

	

cv2.imshow("mpa_line",img)



cv2.waitKey(0)
cv2.destroyAllWindows()


