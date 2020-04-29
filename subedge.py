import cv2
import numpy as np
import random

img = cv2.imread('house.tif', 0)


cv2.imshow('img', img)
m, n = img.shape

k = 3

img1 = np.zeros([(m-k)+1, (n-k)+1], np.uint8)
img2 = np.zeros([(m-k)+1, (n-k)+1], np.uint8)
img3 = np.zeros([(m-k)+1, (n-k)+1], np.uint8)
img4 = np.zeros([(m-k)+1, (n-k)+1], np.uint8)

kernel = [[-1, 0, 1], [-1,0,1], [-1, 0, 1]] 

kernel2 = [[-1, -1, -1], [0,0,0], [1, 1, 1]] 

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
        s0=0
        s1=0
        s2=0
        for a in range(k):
            for b in range(k):
                s0 = s0 + kernel2[a][b]*img[i+a][j+b]

        img2[i][j] = s0


for i in range(m-k):
    for j in range(n-k):
        	if img1[i,j]>=200 :
        		img1[i,j]=0



for i in range(m-k):
    for j in range(n-k):
            if img2[i,j]>=200 :
                img2[i,j]=0



for i in range(m-k):
    for j in range(n-k):
            img4[i,j]=img1[i,j]
            if img1[i,j]>50:
                if img2[i,j]>50:
                    if i-20>0 and j-20>0:
                        for d in range(20):
                            for e in range(20):
                                img4[i-d,j-e]=0 
            if img1[i,j] != img2[i,j] :
                if img1[i,j] > 50 :
                    img3[i,j]=img1[i,j]
                else:
                    img3[i,j]=img2[i,j]



cv2.imshow("verticle",img1)
cv2.imshow("horizontal",img2)
cv2.imshow("fulledge",img3)
cv2.imshow("only",img4)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()



