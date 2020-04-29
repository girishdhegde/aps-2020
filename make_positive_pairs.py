import pandas as pd 
import numpy as np 
import cv2
import os
import random
import pickle

path = './omniglot_train/'

directories = os.listdir(path)

positive_dataset = []

for fldr in directories:
    classes = os.listdir(path + fldr)
    print(fldr)
    for lbl in classes:
        images = os.listdir(path + fldr + './' + lbl)
        print('\t', lbl)
        for i in range(20):
            # img1 = cv2.imread(path + fldr + './' + lbl + './' + random.choice(images), 0)
            img1 = cv2.imread(path + fldr + './' + lbl + './' + images[i], 0)
            img2 = cv2.imread(path + fldr + './' + lbl + './' + random.choice(images), 0)
            # cv2.imshow("img1", img1)
            # cv2.imshow("img2", img2)
            # cv2.waitKey(0)
            positive_dataset.append(np.array([img1 / 255, img2 /255]))


with open("positive_pairs.pkl", 'wb') as file:
    pickle.dump(positive_dataset, file)






