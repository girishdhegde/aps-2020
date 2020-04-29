import math
t=int(input())
for t1 in range(t):
    n,m=map(int,input().split())
    xset=list(map(int,input().split()))
    yset=list(map(int,input().split()))
    xn=[i for i in xset if i<0]
    xp=[i for i in xset if i>0]
    yn=[i for i in yset if i<0]
    yp=[i for i in yset if i>0]
    d1=0
    flag=0
    if 0 in xset:
        d1=n-1
        flag=1
    else:
         d1=n
        
    if 0 in yset:
        d2=m-1
        flag=1
    else:
        d2=m
        
    if flag==1:    
        count=d1*d2
    else:
        count=0
        
    for i in xn:
        for j in xp:
            h=math.sqrt(abs(i*j))
            if h%1 ==0:
                if h in yp:
                    count+=1
                if -1*h in yn:
                    count+=1
                   
                
    for i in yn:
        for j in yp:
            h=math.sqrt(abs(i*j))
            if h%1 ==0:
                if h in xp:
                    count+=1
                if -1*h in xn:
                    count+=1
                    
                
    print(count)