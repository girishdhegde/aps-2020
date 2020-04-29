import cv2
import numpy as np


def dense():

    global cap,currentframe
    if denseflag==1:
        x=currentframe
        x1=x-100
        y1=x+100
        count=x1
        cap.set(1,x1)
        ret, frame1 = cap.read()
        prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
      
        while(count<y1):
            ret, frame2 = cap.read()
            next1 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        
            flow = cv2.calcOpticalFlowFarneback(prvs,next1, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            a=flow[0]
            a=np.sum(np.square(a))
            b=flow[1]
            b=np.sum(np.square(b))
            z=np.sqrt(a+b)
            data.append([count,z])
            print(count)
            #cv2.imshow('frame1',frame1)
            #k = cv2.waitKey(30) & 0xff
            #if k == 27:
            #   break
            prvs = next1
            count+=1
        List = [data[f][1] for f in range(len(data))]
        high=List.index(max(List))
        print(high)
        cap.set(1,data[high][0])
        currentframe = data[high][0]
        ret, frame1 = cap.read()
        cv2.destroyAllWindows()
        cv2.imshow('frame',frame1)
    else :
        print("Check mark optical flow")

temp=[]
data=[]

def left():
    global currentframe,high,List,temp,cap
    if denseflag==1:
        if(high!=0):
            temp=[List[f] for f in range(0,high)]
            high=temp.index(max(temp))
            high=List.index(temp[high])
            print(data[high][0])
            cap.set(1,data[high][0])
            currentframe = data[high][0]
            ret, frame1 = cap.read()
            cv2.destroyAllWindows()
            cv2.imshow('frame',frame1)
        else:
            print("Go right")
    else :
        print("Check mark optical flow")
def right():

    global high,List,cap,currentframe
    if denseflag==1:
        if(high!=199):
            temp=[List[f] for f in range(high+1,200)]
            high=temp.index(max(temp))
            high=List.index(temp[high])
            print(data[high][0])
            cap.set(1,data[high][0])
            currentframe = data[high][0]
            ret, frame1 = cap.read()
            cv2.destroyAllWindows()
            cv2.imshow('frame',frame1)
        else:
            print("Go left")
    else :
        print("Check mark optical flow")
    