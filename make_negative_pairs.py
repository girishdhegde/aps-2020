import pandas as pd 
import numpy as np 
import cv2
import os
import random
import pickle

path = './omniglot_train/'

directories = os.listdir(path)

negative_dataset = []

for fldr in directories:
    classes = os.listdir(path + fldr)
    print(fldr)
    for lbl in classes:
        images = os.listdir(path + fldr + './' + lbl)
        print('\t', lbl)
        for i in range(20):
            # img1 = cv2.imread(path + fldr + './' + lbl + './' + random.choice(images), 0)
            img1 = cv2.imread(path + fldr + './' + lbl + './' + images[i], 0)

            neg_lang = path + random.choice(directories)
            neg_char = neg_lang + './' + random.choice(os.listdir(neg_lang))
            neg_img = neg_char + './' + random.choice(os.listdir(neg_char))

            img2 = cv2.imread(neg_img, 0)
            # cv2.imshow("img1", img1)
            # cv2.imshow("img2", img2)
            # cv2.waitKey(0)
            negative_dataset.append(np.array([img1 / 255, img2 /255]))


with open("negative_pairs.pkl", 'wb') as file:
    pickle.dump(negative_dataset, file)






