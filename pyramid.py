import numpy as np  
import cv2
import random

k=3
p=k
q=k
temp=1
z=1
for t in range(1,100):#calculatu=ion of padding
	temp=temp+2
	if temp==k:
		z=t
		break

print(z)

imgo=cv2.imread('c:/users/girishhegde/iitdimg/house.tif')
cv2.imshow("img",imgo)

filtr=[[1,2,1],[2,4,2],[1,2,1]]
filtr=np.array(filtr)/16
print(filtr)


m,n,o=imgo.shape
'''
img=np.zeros((m+2*z,n+2*z),np.uint8)

for i in range(m):
	for j in range(n):
		img[i+z,j+z]=imgo[i,j]

cv2.imshow("paddedimg",img)

x=m
y=n


img1=np.zeros([m,n],np.uint8)
img2=np.zeros([m,n],np.uint8)
img3=np.zeros([m,n],np.uint8)
img4=np.zeros([m,n],np.uint8)
img5=np.zeros([m,n],np.uint8)
img6=np.zeros([m,n],np.uint8)
'''

def conv2d(abc):

	m1,n1,c1=abc.shape

	temp=np.zeros((m1+2*z,n1+2*z,3),np.uint8)

	for i in range(m1):
		for j in range(n1):
			temp[i+z,j+z]=abc[i,j]

	for i in range(m1):
		for j in range(n1):
			s0=0
			s1=0
			s2=0
			for a in range(-1*(z),(z)+1):
				for b in range(-1*(z),(z)+1):
					s0=s0+temp[i+a,j+b,0]*filtr[a+1,b+1]
					s1=s1+temp[i+a,j+b,1]*filtr[a+1,b+1]
					s2=s2+temp[i+a,j+b,2]*filtr[a+1,b+1]
			temp[i,j,0]=int(s0)
			temp[i,j,1]=int(s1)
			temp[i,j,2]=int(s2)


	return temp


def down(xyz):

	m2,n2,c2=xyz.shape

	temp=np.zeros((m2//2,n2//2,3),np.uint8)

	for i in range(m2//2):
		for j in range(n2//2):
			temp[i,j]=xyz[i*2][j*2]

	return temp



def up(uvw):
	m3,n3,c3=uvw.shape

	temp=np.zeros((m3*2,n3*2,3),np.uint8)
	for i in range(0,m3):
		for j in range(0,n3):
			for l in range(2):
				for m in range(2):
					temp[i*2+l,j*2+m,0]=uvw[i,j,0]
					temp[i*2+l,j*2+m,1]=uvw[i,j,1]
					temp[i*2+l,j*2+m,2]=uvw[i,j,2]

	return temp




x=conv2d(imgo)#blurred op		
cv2.imshow("conv",x)
y=down(x)#downscale
cv2.imshow("down",y)
x2=up(y)#upscale
cv2.imshow("up",x2)
x3=conv2d(x2)#blurring		
cv2.imshow("upconv",x3)
a1,b1,d=x3.shape
yy=x3[:a1-2,:b1-2,:3]
kk=x-yy
cv2.imshow("sub",kk)
cv2.imshow("laplacian",((kk)**2)**0.5)

y2222=up(y)
cv2.imshow("added",y2222+kk)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()



