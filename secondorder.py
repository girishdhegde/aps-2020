import numpy as np 

x=[]
y=[]
for i in range(100):
	x.append(i)
	y.append(2*(i**2)+3*i+5)
	print(x[-1],y[-1])


#y=px2+mx+c
#sy =psx2+ m(sx) + nc
#s(xy) =psx3 + m(sx2) + csx
#syx2 = psx4 + msx3 +csx2


n = len(x)
x = np.array(x)
y =  np.array(y)

sx = np.sum(x)

sx2 = np.sum(x**2)

sx3 = np.sum(x**3)

sx4 = np.sum(x**4)

sy = np.sum(y)
sxy = np.sum(x*y)
syx2 = np.sum(y*(x**2))

print(sx)
print(sx2)
print(sx3)
print(sx4)
print(sxy)
print(syx2)
print(sy)

mb = [sy,sxy,syx2]
ma = [[sx2,sx,n],[sx3,sx2,sx],[sx4,sx3,sx2]]

mp = np.array(ma)
mm = np.array(ma)
mc = np.array(ma)


mp[:,0] = mb

mm[:,1] = mb

mc[:,2] = mb

p = (np.linalg.det([[sy,sx,n],[sxy,sx2,sx],[syx2,sx3,sx2]]))/(np.linalg.det(ma))


m = (np.linalg.det([[sx2,sy,n],[sx3,sxy,sx],[sx4,syx2,sx2]]))/(np.linalg.det(ma))


c = (np.linalg.det([[sx2,sx,sy],[sx3,sx2,sxy],[sx4,sx3,syx2]]))/(np.linalg.det(ma))

print(" y = ",p,"x2 +",m,"x +",c)

