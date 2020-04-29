import cv2
import time

cap = cv2.VideoCapture('3d.mp4')


t=time.time()

currentframe=1

while (time.time()-t) < 10 :

	ret , frame =cap.read()

	filename  = 'd:/frame/frame'+str(currentframe)+'.jpg'
	
	#cv2.imshow('image',frame)
	
	cv2.imwrite(filename,frame)

	currentframe+=1
	time.sleep(1/30)

print("done")

cap.release()
cv2.destroyAllWindows()
