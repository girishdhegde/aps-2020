import numpy as np  
import cv2



k=int(input("kernal size >>"))
p=k
q=k


img=cv2.imread('c:/users/girishhegde/th.jpg')
cv2.imshow("img",img)

m,n,c=img.shape


x=m
y=n


img1=np.zeros([x//p,y//q,3],np.uint8)
kernal0=np.zeros([p,q],np.uint8)
kernal1=np.zeros([p,q],np.uint8)
kernal2=np.zeros([p,q],np.uint8)


for i in range(0,x//p):
	for j in range(0,y//q):
		for a in range(p):
			for b in range(q):
				kernal0[a,b]=img[i*p+a,j*q+b,0]
				kernal1[a,b]=img[i*p+a,j*q+b,1]
				kernal2[a,b]=img[i*p+a,j*q+b,2]

		img1[i,j,0]=np.average(kernal0)
		img1[i,j,1]=np.average(kernal1)
		img1[i,j,2]=np.average(kernal2)

				


cv2.imshow("diminished",img1)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()



