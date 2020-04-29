import cv2
import matplotlib.pyplot as plt 
import numpy as np


img=cv2.imread("c:/users/girishhegde/iitdimg/nature4.jpg",0)
cv2.imshow('img1',img)

tar=cv2.imread("c:/users/girishhegde/iitdimg/nature1.jpeg",0)
cv2.imshow("original",tar)


def match(source,base):

	otype=source.dtype
	oshape=source.shape

	source=source.ravel()
	base=base.ravel()

	s_value,s_index,s_counts=np.unique(source,return_inverse=True,return_counts=True)

	b_value,b_counts=np.unique(base,return_counts=True)

	s=np.cumsum(s_counts).astype(np.float64)
	s/=s[-1]


	b=np.cumsum(b_counts).astype(np.float64)
	b/=b[-1]

	interpolate=np.interp(s,b,b_value)
	interpolate=interpolate.astype(otype)

	return interpolate[s_index].reshape(oshape)

def equhist(ipimg):

	x,y=ipimg.shape

	temp=np.zeros(ipimg.shape,np.uint8)

	h=np.zeros(256)

	for  i in range(x):
		for j in range(y):
			h[ipimg[i][j]]=h[ipimg[i][j]]+1
	H=h.copy()

	#plt.subplot(2,1,1)
	#plt.bar([i for i in range(256)],h)
	
	#plt.show()
	
	h=h/(x*y)

	for  i in range(1,256): 
		h[i]=h[i]+h[i-1]

	h=h*255

	#plt.subplot(2,1,2)
	#plt.bar([i for i in range(256)],h)
	#plt.show()

	for  i in range(x):
		for j in range(y):
				temp[i][j]=h[ipimg[i][j]]


	return [temp,H,h]




out=match(tar,img)
cv2.imshow('hist',out)
cv2.imwrite("histmatch.jpg",out)

a,b,c=equhist(out)
cv2.imshow('hista',a)
e,f,g=equhist(img)

cv2.imshow('histe',e)
plt.subplot(2,1,1)
plt.bar(range(256),b)
plt.subplot(2,1,2)
plt.bar(range(256),f)
plt.show()

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()
		

