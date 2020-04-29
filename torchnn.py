import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

x = torch.tensor([1.0 , 11.5])
h = torch.tensor([1.0 , 2.0 , 3.0])
y = torch.tensor([0.0,1.0])

w1 = torch.tensor([[.1,.2],[.3,.2]] , requires_grad = True)
w2 = torch.tensor([[.5,.9],[0.5,0.7],[.4,.4]] , requires_grad = True)



print("x:\n",x)
print("w1:\n",w1)

z1 = torch.matmul(x , w1)
print("z1:\n",z1)

h[1:] = torch.relu(z1)
print("h1:\n",h)
print("w2:\n",w2)


z2 = torch.matmul(h , w2)

a2 = torch.sigmoid(z2)

print("z2:\n",z2)
print("a2:\n",a2)

criterion = nn.BCELoss(reduction='sum')

loss = criterion(a2 , y)
loss.backward()

print("loss:\n",loss) 

print("w1.data:\n",w1.data)

print("w1.grad:\n",w1.grad)


print("w2.data:\n",w2.data)

print("w2.grad:\n",w2.grad)


alpha = 0.001
w1.data = w1.data - alpha*w1.grad
w2.data = w2.data - alpha*w2.grad


print("udated weights:")
print(w1)
print(w2)