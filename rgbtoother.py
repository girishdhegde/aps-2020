import cv2
import numpy as np 


img=cv2.imread("c:/users/girishhegde/th.jpg")

x,y,z=img.shape


img1=np.zeros([x,y,3],np.uint8)

img2=np.zeros([x,y,3],np.uint8)

img3=np.zeros([x,y,3],np.uint8)

gray=np.zeros([x,y],np.uint8)

bnw=np.zeros([x,y],np.uint8)

neg=np.zeros([x,y,3],np.uint8)


neg=255-img

for i in range(x):
	for j in range(y):
		img1[i,j,0]=img[i,j,0]
		img2[i,j,1]=img[i,j,1]
		img3[i,j,2]=img[i,j,2]
		gray[i,j]=(img[i,j,0]/3+img[i,j,1]/3+img[i,j,2]/3)
		if gray[i,j]>127:
			bnw[i,j]=255


cv2.imshow("img",img)

cv2.imshow("img1",img1)
cv2.imwrite("blue.jpg",img1)
cv2.imshow("img2",img2)
cv2.imwrite("green.png",img2)
cv2.imshow("img3",img3)
cv2.imwrite("red.tiff",img3)
cv2.imshow("gray",gray)
cv2.imwrite("c:/users/girishhegde/iitdimg/gray.jpg",gray)
cv2.imshow("bnw",bnw)
cv2.imshow("neg",neg)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()