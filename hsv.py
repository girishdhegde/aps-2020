import cv2
import numpy as np 


img=cv2.imread("c:/users/girishhegde/th.jpg")

x,y,z=img.shape


hsv=np.zeros([x,y,3],np.uint8)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

img1=np.zeros([x,y],np.uint8)
img2=np.zeros([x,y],np.uint8)

img3=np.zeros([x,y],np.uint8)

#y=np.zeros([x,y],np.uint8)

#cb=np.zeros([x,y],np.uint8)

#cr=np.zeros([x,y],np.uint8)
img4=np.zeros([x,y],np.uint8)
img5=np.zeros([x,y],np.uint8)
img6=np.zeros([x,y],np.uint8)


ycc=np.zeros([x,y,3],np.uint8)

ycc=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
'''

neg=255-img

for i in range(x):
	for j in range(y):
		img1[i,j,0]=img[i,j,0]
		img2[i,j,1]=img[i,j,1]
		img3[i,j,2]=img[i,j,2]
		gray[i,j]=(img[i,j,0]+img[i,j,1]+img[i,j,2]/3
		if(img[i,j,0]>127):
			bnw[i,j]=255


cv2.imshow("img",img)

cv2.imshow("img1",img1)
cv2.imwrite("blue.jpg",img1)
cv2.imshow("img2",img2)
cv2.imwrite("green.png",img2)
cv2.imshow("img3",img3)
cv2.imwrite("red.tiff",img3)
cv2.imshow("gray",gray)
cv2.imwrite("gray",gray)
cv2.imshow("bnw",bnw)
'''
for i in range(x):
	for j in range(y):
		img1[i,j]=hsv[i,j,0]
		img2[i,j]=hsv[i,j,1]
		img3[i,j]=hsv[i,j,2]
		img4[i,j]=ycc[i,j,0]
		img5[i,j]=ycc[i,j,1]
		img6[i,j]=ycc[i,j,2]





	
cv2.imshow("img",img)
cv2.imshow("hsv",hsv)
cv2.imshow("h",img1)
cv2.imshow("s",img2)
cv2.imshow("v",img3)
#cv2.imshow("cb",cb)
#cv2.imshow("cr",cr)
cv2.imshow("yuv",ycc)

cv2.imshow("cr",img5)
cv2.imshow("cb",img6)
cv2.imshow("Y",img4)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()