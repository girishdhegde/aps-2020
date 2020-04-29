import numpy as np
x = [1,2,3,4,5]
y = [2,4,6,8,10]
t0=0
t1=1
alpha = 0.1

def hyp(x):
	global t0,t1
	h = []
	for i in x:
		h.append(t0 + t1 * i)
	return h

dif = []
h = []
for iter in range(5):
	h = hyp(x)
	dif = np.array(h) - np.array(y)
	difx = np.array(dif) * np.array(x)
	sumdif = np.sum(np.array(dif))
	sumdifx = np.sum(np.array(difx))
	t0 = t0 - alpha * sumdif / 5
	t1 = t1 - alpha * sumdifx / 5
	print("h",h)
	print("dif",dif)
	print("difx",difx)
	print("sumdif=",sumdif)
	print("sumdifx=",sumdifx)
	print("t0=",t0)
	print("t1=",t1)
	print("\n\n\n")  

