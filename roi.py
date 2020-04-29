import cv2
import numpy as np 

xy=[]
i=0

def rect(event,x,y,flags,param):
	global xy,i
	if event==cv2.EVENT_LBUTTONDOWN:
		font=cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img,str([x,y]),(x,y),font,0.75,(0,255,0),1,cv2.LINE_AA)
		cv2.imshow("image",img)
		i=i+1
		xy.append((x,y))
		if i==2:
			i=0
			cv2.rectangle(img,xy[0],xy[1],[0,0,255],5)
			cv2.imshow("image",img)
			xy=[]
					
		


img=cv2.imread("c:/users/girishhegde/iitdimg/dog2.jpg")
cv2.imshow("image",img)

cv2.setMouseCallback('image',rect)


cv2.waitKey(0)
cv2.destroyAllWindows()