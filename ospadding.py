import cv2
import numpy as np    

import matplotlib.pyplot as plt
img=cv2.imread('c:/users/girishhegde/th.jpg')
cv2.imshow("img",img)



n,m,c=img.shape

#3*3 => kernal   ,,,, jumping
p=20
q=20

'''if m%q :
	x=m//q
	x=(x+1)*q

if n%p :
	y=n//p
	y=(y+1)*p
'''
img1=np.zeros([n+2*p,m+2*q,3],np.uint8)

for i in range(n):
	for j in range(m):
		img1[i+p,j+q,0]=img[i,j,0]
		img1[i+p,j+q,1]=img[i,j,1]
		img1[i+p,j+q,2]=img[i,j,2]
		




img2=np.zeros([n,m,3],np.uint8)
img2=img2+255
for i in range(n-p):
	for j in range(m-q):
		img2[i+p//2,j+q//2,0]=img[i+p,j+q,0]
		img2[i+p//2,j+q//2,1]=img[i+p,j+q,1]
		img2[i+p//2,j+q//2,2]=img[i+p,j+q,2]

cv2.imshow("0spadding",img1)
cv2.imshow("crop",img2)


k=cv2.waitKey(0)

if k==27:
	cv2.destroyAllWindows()