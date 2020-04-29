import numpy as np  
import cv2
import random


k=int(input("enter the thickness >>"))
p=k
q=k


imgo=cv2.imread('789.png',0)
#ch=int(input("0:dilation,1:erosion >>"))
cv2.imshow("img",imgo)
print(imgo.shape)

m,n=imgo.shape


x=m
y=n


if m%p :
	w=m//p
	x=w*p+p

if n%q :
	w=n//q
	y=(w*q)+q

X=x
Y=y

img1=np.zeros([x,y],np.uint8)
img2=np.zeros([x,y],np.uint8)
img3=np.zeros([x,y],np.uint8)
img4=np.zeros([x,y],np.uint8)
print(img1.shape)
kernal0=np.zeros([p,q],np.uint8)

def erosion(img):
	global x,y
	m,n=img.shape
	temp=np.zeros([x,y],np.uint8)
	for i in range(m):
		for j in range(n):
			temp[i,j]=img[i,j]
	for i in range(0,x//p):
		for j in range(0,y//q):
			flag=0
			for l in range(i*p,i*p+p):
				for m in range(j*q,j*q+q):
					if temp[l,m]==0:
						flag=1
						break
				if flag==1:
					break
			if flag==1:
			   	for l in range(i*p,i*p+p):
			   		for m in range(j*q,j*q+q):
			   			temp[l,m]=0

	return temp



def dilation(img):
	r,s=(img.shape)
	global x,y
	temp=np.zeros([x,y],np.uint8)
	for i in range(0,r):
		for j in range(0,s):
			temp[i,j]=img[i,j]
	print(temp.shape)
	for i in range(0,r):
		for j in range(0,s):
			temp[i,j]=img[i,j]
	for i in range(0,x//p):
		for j in range(0,y//q):
			flag=0
			for l in range(i*p,i*p+p):
				for m in range(j*q,j*q+q):
					if temp[l,m]==255:
						flag=1
						break
				if flag==1:
					break
			if flag==1:
			   	for l in range(i*p,i*p+p):
			   		for m in range(j*q,j*q+q):
			   			temp[l,m]=255
	return temp




img1=erosion(imgo)
img2=dilation(imgo)

img3=dilation(img1)

img4=erosion(img2)


cv2.imshow("eroision",img1)

cv2.imshow("dilation",img2)


cv2.imshow("opening",img3)

cv2.imshow("closing",img4)


k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()



