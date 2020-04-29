import numpy as np
import matplotlib.pyplot as plt
import random

#x1 = [1,2,3,4,5,6,7,8,9,30,31,32,34,35,36,37]
#x2 = [5,5,5,5,5,5,5,5,5,10,10,10,10,10,10,10]

#x1 = np.random.rand(100)*100
#x2 = np.random.rand(100)*100

#daa generation

x1 =[]
x2 = []
for i in range(50):
	x = random.randint(0,100)
	y = random.randint(0,20)

	a = random.randint(0,100)
	b = random.randint(50,100)
	
	x1.append(x)
	x2.append(y)

	x1.append(a)
	x2.append(b)




m = len(x1)

centroid = [[x1[0],x2[0]],[x1[-1],x2[-1]]]
print(centroid)



def mean(gp):
	return [np.sum((np.array(gp))[:,0])/len(gp),np.sum((np.array(gp))[:,1])/len(gp)]


def distance(point1,point2):
	return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5


def group(centroid,x_1,x_2):
	group1 = []
	group2 = []
	for x,y in zip(x_1,x_2):
		if distance(centroid[0],[x,y]) < distance(centroid[1],[x,y])  :
			group1.append([x,y])
		else :
			group2.append([x,y])

	return [group1,group2,[mean(group1),mean(group2)]]


def cluster(x,y):
	if distance(centroid[0],[x,y]) < distance(centroid[1],[x,y])  :
		return 1
	else :
		return 2


old_centroid = [[0,0],[0,0]]




#training
while old_centroid != centroid :
	old_centroid = centroid
	new = group(centroid,x1,x2)
	centroid = new[2]
	print(centroid)




#ploting
gp1,gp2,c=group(centroid,x1,x2)

plt.scatter((np.array(gp1))[:,0],(np.array(gp1))[:,1])

plt.scatter((np.array(gp2))[:,0],(np.array(gp2))[:,1])

plt.scatter((np.array(c))[:,0],(np.array(c))[:,1])

plt.show()


