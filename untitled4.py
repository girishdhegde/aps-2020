# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:50:18 2019

@author: Tushar
"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0)
# Create old frame
_, frame = cap.read()
old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

flag = 0
# Lucas kanade params
lk_params = dict(winSize = (20,20),
                 maxLevel = 4,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))




point_selected = False
point = ()
flag=0
xx=0
#yy=0
old_points = np.array([[]])

#old_points = np.array([[xx, yy]], dtype=np.float32)
th1=100
th2=100

        
      #old_points1=np.array(list(old_points).append([x,y]),dtype=np.float32)


# Mouse function
def select_point(event, x, y, flags, params):
    global flag
    global point, point_selected, old_points,flag,xx,old_gray,cap,frame
    if event == cv2.EVENT_LBUTTONDOWN:

        point = (x, y)
        point_selected = True
        old_points1 = np.array([[x, y]], dtype=np.float32)
        print(flag,point_selected)
        if flag==1:
            old_points=np.concatenate((old_points,old_points1))
            xx=np.concatenate((xx,old_points1))
            
        else:
            old_points=old_points1
            xx=old_points1
            flag=1

        ff()

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", select_point) 


def ff():
    global flag
    global point, point_selected, old_points,flag,xx,old_gray,cap,frame
    new_points = []
    while True:
        _, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if point_selected is True:
            cv2.circle(frame, point, 5, (0, 0, 255), 2)
            new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_points, None, **lk_params)
            old_gray = gray_frame.copy()
            
            z=new_points-xx
            z1=z[:,0]
            z2=z[:,1]
            for f in range(len(z1)):
                if  z1[f]>th1: 
                    print("enter 'h' for label or any key to continue")
                    key=cv2.waitKey(0)
                    if(key==ord('h')):
                        label(i)
                if  z2[f]>th2:
                    print("enter 'v' for label or any key to continue")
                    key=cv2.waitKey(0)
                    if(key==ord('v')):
                        label(i)
                if z1[f] >th1 and z2[f]>th2:
                    print("enter 'd' for label or any key to continue")
                    key=cv2.waitKey(0)
                    if(key==ord('d')):
                        label(i)
                    

            
            for i,(new,old) in enumerate(zip(new_points,old_points)):
                x,y = new.ravel()
                c,d = old.ravel()
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            old_points = new_points
            #x, y = new_points.ravel()
            #
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            print(xx)
            print("hi")
            print(new_points)
            break

ff()
cap.release()
cv2.destroyAllWindows()