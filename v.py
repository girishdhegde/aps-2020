Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@girishdhegde 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


klvijeth
/
code_snippets
1
00
 Code Issues 0 Pull requests 0 Actions Projects 0 Wiki Security Insights
code_snippets/stable_marriage.py / 
@klvijeth klvijeth Create stable_marriage.py
f9669d4 12 hours ago
74 lines (73 sloc)  1.11 KB
  
You're using code navigation to jump to definitions or references.
Learn more or give us feedback
n=int(input())
male=[]
female=[]
pro={}
mar={}
mar1={}
def func(qq):
    global male
    global female
    global pro
    global mar
    global mar1
    global n
    flag=0
    count=0
    while(flag==0):
        x=male[qq]
        m=min(x)
        ind=x.index(m)
        x[ind]=2*n
        male[qq][ind]=2*n
        if(ind not in mar):
            pro[ind]=1
            mar[ind]=female[ind][qq]
            mar1[ind]=qq
            flag1=1
            return
        else:
            pro[ind]+=1
            if(female[ind][count]<mar[ind]):
                mar[ind]=female[ind][count]
                xx=mar1[ind]
                mar1[ind]=qq
                func(xx)
                return
for i in range(n):
    l=list(map(int,input().split()))
    male.append(l)
for i in range(n):
    l=list(map(int,input().split()))
    female.append(l)
count=0
for i in male:
    flag=0
    while(flag==0):
        x=i
        m=min(x)
        ind=x.index(m)
        x[ind]=2*n
        male[count][ind]=2*n
        if(ind not in mar):
            mar[ind]=female[ind][count]
            mar1[ind]=count
            flag=1
            pro[ind]=1
            break
        else:
            pro[ind]+=1
            if(female[ind][count]<mar[ind]):
                flag=1
                mar[ind]=female[ind][count]
                xx=mar1[ind]
                mar1[ind]=count
                func(xx)
                break
    count+=1
q=int(input())
for i in range(q):
    x=int(input())-1
    if(x in pro):
        print(pro[x])
    else:
        print(0)
        
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
