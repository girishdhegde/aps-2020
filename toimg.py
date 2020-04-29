import pandas as pd 
import numpy as np 
import cv2
import os



path = "./kannada_dataset/train.csv"
# read train data
xy = pd.read_csv(path)
data = np.array(xy)
labels = data[:,0]
dataset = []

foldr_path = "./kannada_dataset/"

flag = 0

print("creating directories ....")
for label in set(labels):
    if not(os.path.isdir(foldr_path + str(label))):
        flag = 1
        os.mkdir(foldr_path + str(label))
print("done")


file_index = np.zeros(len(set(labels)), np.uint32)

if flag == 1:
    print("writing images :")
    for i in range(len(data)):
        img = np.reshape(data[i , 1:] , (28 , 28)).astype(np.uint8)
        cv2.imwrite(foldr_path + str(labels[i]) + '/' + str(file_index[labels[i]]) + '.png', img)
        file_index[labels[i]] += 1
    print("done")


