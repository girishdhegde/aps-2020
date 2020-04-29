import numpy as np 
import matplotlib.pyplot as plt




degree = 1
alpha = 0.01


x=[]
y=[]
x = [1,2,3,4,5]
y = [2,4,6,8,10]
#y = 7x2 + 3x +5

#data generation
'''
for i in range(100):
	x.append(i)
	y.append(7*(i**2)+3*i+5) 
	print(x[-1],y[-1])
'''

def equ(X):
	return 7*(X**2)+3*X+5


#initialization

m = len(x)
x = np.array(x)
y =  np.array(y)
theta = np.random.rand(degree+1)*10
print("initial theta : ",theta)
dj_dt = np.zeros(degree+1,dtype = np.float32)

tx=[]
ty=[]

j=100


def hyp(x):
	h = 0
	for i,t in enumerate(theta):
		h = h + (x**i)*t
	return h

#gradient descent




while j > 0.01 :	
	hypothesis=np.zeros(m,dtype=np.float32)
	for i,t in enumerate(theta) :
		hypothesis = hypothesis + (x**i)*t

	dif = hypothesis - y
	dif_square = dif*dif
	j = (np.sum(dif_square))/(2*m)
	
	print("cost = ",j)

	for i in range(degree+1):
		dj_dt[i] = np.sum(dif*(x**i))/m
	theta = theta - alpha*dj_dt

	tx.append(theta[1])
	ty.append(j)




print("new theta:",theta)
#print(hypothesis)
#print(y)
'''
for  i in range(100,200):
	print(hyp(i),equ(i))
'''
plt.plot(tx,ty)
plt.show()

