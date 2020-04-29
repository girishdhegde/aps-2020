from torch.utils.data import Dataset, DataLoader
from torch import from_numpy, tensor
import numpy as np
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
import pandas as pd
import pickle 
import matplotlib.pyplot as plt
import cv2
from scipy.signal import correlate2d, convolve2d
import PIL
import torchvision
import matplotlib as mpl
from collections import defaultdict
import seaborn as sn

bsize = 100

#read train data

with open('./kannada_dataset/kmnist_train_img.pkl','rb') as file:
    data = pickle.load(file)

with open('./kannada_dataset/kmnist_train_lbl.pkl','rb') as file:
    lbl = pickle.load(file)

data = data.reshape(lbl.shape[0], 1, 28, 28)

#shuffling of data and label
index = np.arange(lbl.shape[0])
np.random.shuffle(index)

data = data[index]
lbl  = lbl[index ]



x_data = from_numpy(data)
y_data = from_numpy(lbl)

bathes  = int(np.ceil(data.shape[0] / bsize))


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)    
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.mp = nn.MaxPool2d(2)
        self.fc = nn.Linear(20*4*4, 10)

    def forward(self, x):
        in_size = x.size(0)                   # conv -> x * x -> (x - (kernel_size - 1)) * (x - (kernel_size - 1))
        x = F.relu(self.mp(self.conv1(x)))    # 28*28 -> 24*24 -> 12*12 -> 12*12 
        x = F.relu(self.mp(self.conv2(x)))    # 12*12 -> 8 * 8 -> 4 * 4 -> 4 * 4
        #to 1d i.e reshape
        x = x.view(in_size, -1) 
        x = self.fc(x)
        #return F.log_softmax(x)

        return x

# out1 = model.conv1(Variable(x_data[0:1]).cuda())
# out2 = model.mp(out1)
# out3 = model.conv2(out2)
# out4 = model.mp(out3)

# #print(out1)
# print(out1.shape)

# #print(out2)
# print(out2.shape)

# #print(out3)
# print(out3.shape)

# #print(out4)
# print(out4.shape)



model = Net()


criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)


if torch.cuda.is_available():
    model = model.cuda()
    criterion = criterion.cuda()
    
print(model)


def train(epoch):

    for batch in range(bathes - 1):

        start = batch * bsize

        data = x_data[start : start + bsize]
        target = y_data[start : start + bsize]

        #if torch.cuda.is_available():
        data   = data.cuda()
        target = target.cuda()
        #print(data.shape)

        optimizer.zero_grad()

        output = model(data)
        loss   = criterion(output , target)
        losses.append(loss)

        loss.backward()
        optimizer.step()



        print('[Epoch , batch] : [', epoch + 1 ,"/", epochs ,"][" , batch + 1 , "/",bathes,"]\tloss : " , loss.item())

losses = []

# model.load_state_dict(torch.load("weights_w.pt"))
# model.eval()

epochs = 1
for epoch in range(epochs):
    train(epoch)


#torch.save(model.state_dict() , "weights_w.pt")

















###############################################################################################
#PLOTING

plt.plot(losses)
plt.ylabel("loss")
plt.xlabel("epoch")
plt.show()
# plt.savefig("trainingloss.png")


correct = 0
total = 0
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
errors_imgs=[]
errors_labels=[]
confusion_matrix = torch.zeros(10, 10)
err_confusion_matrix = torch.zeros(10, 10)
correct_samples={i:None for i in range(10)}
with torch.no_grad():
    for b in range(bathes - 1):
        start = b * bsize
        data = [x_data[start : start + bsize] , y_data[start : start + bsize]]
        images, labels = data[0].to(device), data[1].to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        errors_imgs.extend(images[predicted != labels])
        errors_labels.extend(zip(predicted[predicted != labels], labels[predicted != labels]))
        
        for i in [i for i in correct_samples if type(correct_samples[i]) != torch.Tensor]:
            ci = images[(predicted == labels) & (i == labels)]
            if ci.shape[0] > 0:
                correct_samples[i] = ci[0]
        for t, p in zip(labels.view(-1), predicted.view(-1)):
            confusion_matrix[t.long(), p.long()] += 1
            if t.long() != p.long():
                err_confusion_matrix[t.long(), p.long()] += 1
errors_imgs=torch.stack(errors_imgs)
errors_labels=np.array([(p.item(), t.item())for p, t in errors_labels])
print('accuracy of the network on the test images: %d %%' % (100 * correct / total))



print('errors: ',len(errors_labels))

df_cm = pd.DataFrame(confusion_matrix.numpy(), range(10), range(10))

plt.figure(figsize = (20,20))
plt.title("confusion_matrix")
sn.set(font_scale=2)
sn.heatmap(df_cm, annot=True,annot_kws={"size": 14}, fmt='g')


df_cm = pd.DataFrame(err_confusion_matrix.numpy(), range(10), range(10))

plt.figure(figsize = (20,20))
plt.title("error_confusion_matrix")
sn.set(font_scale=2)
sn.heatmap(df_cm, annot=True,annot_kws={"size": 14}, fmt='g')

sn.set(font_scale=1)
sn.set_style("whitegrid", {'axes.grid' : False})

f=lambda i, a: ({k: len(v) for k, v in a.items()} if [a[x].append(i) for x in i] else {})

errors=f(errors_labels[:,1],defaultdict(list))


plt.figure(figsize=(6,4))
plt.barh(*zip(*errors.items()))
plt.yticks(range(10))
plt.xlabel('erorrs')
plt.ylabel('labels')
plt.show()

