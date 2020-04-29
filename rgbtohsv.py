import cv2
import numpy as np 
import math

img=cv2.imread("c:/users/girishhegde/th.jpg")

x,y,z=img.shape


h=np.zeros([x,y],np.uint8)

s=np.zeros([x,y],np.uint8)

v=np.zeros([x,y],np.uint8)

a=np.zeros([x,y],np.uint8)
b=np.zeros([x,y],np.uint8)

y=np.zeros([x,y],np.uint8)
cb=np.zeros([x,y],np.uint8)
cb=np.zeros([x,y],np.uint8)

#neg=np.zeros([x,y,3],np.uint8)




for i in range(x):
	for j in range(y):
		v[i,j]=(img[i,j,0]/3+img[i,j,1]/3+img[i,j,2]/3)
		cb[i,j]=0.299+

		#if img[i,j,0]/3+img[i,j,1]/3+img[i,j,2]/3 !=0:
		#	s[i,j]=1-(3)*float(np.min(np.array([img[i,j,0],img[i,j,1],img[i,j,2]])))/float((img[i,j,0]+img[i,j,1]+img[i,j,2]))
		#h[i,j]=math.acos((0.5*(img[i,j,2]-img[i,j,0]-img[i,j,1]))/(((img[i,j,2]-img[i,j,1])**2+(img[i,j,2]-img[i,j,0])*(img[i,j,1]-img[i,j,0]))**0.5))
y=v

cv2.imshow("img",img)

cv2.imshow("h",h)
cv2.imshow("s",s)
cv2.imshow("v",v)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()