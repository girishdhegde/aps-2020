import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
import pandas as pd 
import numpy as np

bsize  = 10

f = pd.read_csv("iris_training.csv")
f = np.array(f)

ip = f[:,:4]
op = f[:,4]

index = np.arange(ip.shape[0])
np.random.shuffle(index)

ip = ip[index].astype(np.float32)
op = op[index].astype(np.int64)

ip = torch.from_numpy(ip)
op = torch.from_numpy(op)

class iris(nn.Module):
    def __init__(self):
        super(iris, self).__init__()
        self.layer1 = nn.Linear(4,20)
        self.layer2 = nn.Linear(20,100)
        self.layer3 = nn.Linear(100,20)
        self.layer4 = nn.Linear(20,3)

    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = F.relu(self.layer3(x))
        x = (self.layer4(x))
        #x=F.log_softmax(x)
        return x

net = iris()
print(net)

criterion = nn.CrossEntropyLoss() 
optimizer = optim.Adam(net.parameters(), lr=1e-3) 


net = net.cuda()
criterion = criterion.cuda()

print("inputs:" , ip)
print("labels:" , op)

epochs = 10
batches  = int(np.ceil(ip.shape[0] / bsize))


for epoch in range(epochs):

    for batch in range(batches - 1):

        start = batch * bsize

        data, target = Variable(ip[start : start + bsize]), Variable(op[start : start + bsize])

        data =  data.cuda()
        target = target.cuda()

        optimizer.zero_grad()
        outputs = net(data)
        loss = criterion(outputs, target)
        loss.backward()
        optimizer.step()

        print('[Epoch , batch] : [', epoch + 1 ,"/", epochs ,"][" , batch + 1 , "/",batches,"]\tloss : " , loss.item())

print('Finished Training')

 
ft=pd.read_excel("iris_test.xlsx")
ft=np.array(ft)

ip=ft[:,:4]
op=ft[:,4]

test_names = ['setosa','versicolor','virginica']

print("\n\n\nTESTING:\n")

ipt = Variable(torch.Tensor(ip)).cuda()
oput = net(ipt)
oput = oput.cpu()
opt = np.array(oput.data)

for i,out in enumerate(opt):
    print("prediction = ",test_names[np.argmax(out)] ,"  ;  " , "actual = "  , test_names[int(op[i])])