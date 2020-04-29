import cv2
import numpy as np 


img=cv2.imread("c:/users/girishhegde/th.jpg")

x,y,z=img.shape


t1=85
t2=170

img1=np.zeros([x,y,3],np.uint8)
gray=np.zeros([x,y],np.uint8)

for i in range(x):
	for j in range(y):
		img1[i,j]=img[i,j]
		gray[i,j]=(img[i,j,0]/3+img[i,j,1]/3+img[i,j,2]/3)
		if gray[i,j]<t1:
			img1[i,j,0]=255
			img1[i,j,1]=0
			img1[i,j,2]=0

		elif gray[i,j]>t1 and gray[i,j]<t2:
			img1[i,j,1]=255
			img1[i,j,0]=0
			img1[i,j,2]=0
		else:
			img1[i,j,2]=255
			img1[i,j,0]=0
			img1[i,j,1]=0

			


cv2.imshow("img",img)

cv2.imshow("img1",img1)
cv2.imwrite("segment.jpg",img1)
cv2.imshow("gray",gray)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()