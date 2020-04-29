import numpy as np 
import matplotlib.pyplot as plt


x=[]
y=[]
for i in range(100):
	x.append(i)
	y.append(3*i+5)
	print(x[-1],y[-1])

#y=mx+c
#sy = m(sx) + nc
#s(xy) = m(sx^2) + csx

n = len(x)
x = np.array(x)
y =  np.array(y)


sumx = np.sum(x)
sumxs = np.sum((x**2))
sumy = np.sum(y)
sumxy = np.sum(x*y)

deta = (np.linalg.det([[sumx,n],[sumxs,sumx]]))


m = (np.linalg.det([[sumy,n],[sumxy,sumx]]))/deta
c = (np.linalg.det([[sumx,sumy],[sumxs,sumxy]]))/deta

print(" y = ",m,"x +",c)

