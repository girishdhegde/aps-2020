import numpy as np 
from sklearn.decomposition import  PCA

ip = [[1   , 2  ,1],
     [4   , 5  ,2],
     [3   , 4 ,3 ],
     [2.8 , 4  ,5],
     [1.5 , 3.2,6]]

x = np.array(ip)

x = x - np.mean(x , axis = 0)

# a = np.sum(x[:,0] ** 2)
# b = np.sum(x[:,1] ** 2)
# ab = np.sum(x[:,0] * x[:,1])
# cov = [[ a , ab],
#        [ ab, b ]]

# cov = (np.array(cov) / (len(x) - 1))
print(np.matmul(x.T ,x) / (len(x) - 1))
print(np.cov(x.T))
cov = np.cov(x.T)


eigvalues , eigvecs = np.linalg.eig(cov)

print(eigvecs,eigvalues)

values = (np.sort(eigvalues)[::-1])

pcas = [[],[],[],[],[]]

for i,s in enumerate(x):
    print(s,eigvecs)  
    pcas[i]  = np.matmul(s , eigvecs)


print((pcas))


pc =  PCA(n_components = 3)
print(pc.fit_transform(x))

