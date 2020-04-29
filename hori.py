import cv2
import numpy as np
import random

img = cv2.imread('house.tif', 0)


cv2.imshow('img', img)
m, n = img.shape

k = 3

img1 = np.zeros([(m-k)+1, (n-k)+1], np.uint8)

 #kernel = [[1, 2, 1], [2, 4, 2], [1, 2, 1]] #gussianBlur
kernel = [[-1, -1, -1], [0,0,0], [1, 1, 1]] #sharpen
#kernel= [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]] #edgeDetection
#kernel = np.array(kernel)
#kernel = kernel/16


for i in range(m-k):
    for j in range(n-k):
        s0=0
        s1=0
        s2=0
        for a in range(k):
            for b in range(k):
                s0 = s0 + kernel[a][b]*img[i+a][j+b]

        img1[i][j] = s0
for i in range(m-k):
    for j in range(n-k):
    	#if img1[i,j]>=0 and img1[i,j]<150:
    	#	img1[i,j]=0
    	if img1[i,j]>=200:
    		img1[i,j]=0
cv2.imshow("hwithout",img1)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()



