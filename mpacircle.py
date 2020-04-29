import cv2
import numpy as np 
import math


img=np.zeros((700,700),np.uint8)
#cv2.imshow("img",img)
yl=699
xl=699

x0=370 #centre
y0=300
r=275  #radius

img[yl-(y0+r),(x0+0)]=255

#x=1
y=r

d=5/4-r

for x in range(1,r):
	if x==y-1:
		break

	if d<0:
		d=d+2*x-1                    #d=d+2*(x-1)+1=d+2x-1
	else:
		d=d+2*(x-y)-1                #d=d+2*(x-1)-2*(y)+1
		y=y-1
	
	img[yl-(y0+y),(x0+x)]=255
	img[yl-(y0+x),(x0+y)]=255
	img[yl-(y0-y),(x0-x)]=255
	img[yl-(y0+y),(x0-x)]=255
	img[yl-(y0-y),(x0+x)]=255
	img[yl-(y0-x),(x0+y)]=255
	img[yl-(y0+x),(x0-y)]=255
	img[yl-(y0-x),(x0-y)]=255
	

	

cv2.imshow("mpa_circle",img)



cv2.waitKey(0)
cv2.destroyAllWindows()


