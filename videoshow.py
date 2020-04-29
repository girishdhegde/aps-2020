import cv2
import time


t=time.time()

currentframe=1


img=cv2.imread("dog2.jpg")
cv2.imshow('image',img)

while (time.time()-t) < 10 :

	frame = cv2.imread("d:/frame/frame"+str(currentframe)+".jpg")
	
	#cv2.imshow('image',img)

	currentframe+=1
	
	time.sleep(1/30)

print("done")
cv2.waitKey(0)
cv2.destroyAllWindows()
