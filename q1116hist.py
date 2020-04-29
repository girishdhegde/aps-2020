import cv2
import matplotlib.pyplot as plt 
import numpy as np


img=cv2.imread("c:/users/girishhegde/img1.jpg",0)
cv2.imshow('img1',img)

h=np.zeros(256)

x,y=img.shape
imgh=np.zeros(img.shape,np.uint8)
print(x,'x',y)

for  i in range(x):
	for j in range(y):
		h[img[i][j]]=h[img[i][j]]+1
H=h
plt.bar([i for i in range(256)],h)
plt.show()
h=h/(x*y)


for  i in range(1,256): 
	h[i]=h[i]+h[i-1]

h=h*255
'''
plt.subplot(1,1)
plt.bar([i for i in range(256)],h)
plt.subplot(1,2)
'''
plt.bar([i for i in range(256)],h)
plt.show()

for  i in range(x):
	for j in range(y):
			imgh[i][j]=h[img[i][j]]
print('done')

clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8,))
c=clahe.apply(img)
hi=cv2.equalizeHist(img)
cv2.imshow("cv hist",hi)

cv2.imshow("dif",hi-imgh)


cv2.imshow("clahe",c)

cv2.imshow('hist',imgh)
k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()
