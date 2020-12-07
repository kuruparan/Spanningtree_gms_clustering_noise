import os
from matplotlib.image import imread
import numpy as np
from gms import GmsMatcher
from gms import Size
from gms import DrawingType
import math
from enum import Enum
import cv2
import pickle
cv2.ocl.setUseOpenCL(False)

def computefeat(temp,direcX):
    feature = [[0 for i in range(len(temp))] for j in range(len(temp))] 

    for i in range(0,len(temp)):
        for j in range(i+1,len(temp)):
            img1 = (np.array(direcX[i]))
            img2 = (np.array(direcX[j]))

            if(i==j):
                continue

            if(i!=j):
                orb = cv2.ORB_create(10000)
                orb.setFastThreshold(0)
                if cv2.__version__.startswith('3'):
                    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
                else:
                    matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)
                gms = GmsMatcher(orb, matcher)

                matches = gms.compute_matches(img1, img2)
                           
                feature[i][j]=len(matches)
                feature[j][i] = len(matches)
    return feature

data_src= '/home/kuru/Desktop/market/image_train/'
save_dir = '/home/kuru/Desktop/market/gms/'
X = []
y = []
direcX=[]
direcy=[]
F=[]
id=[]
k=0
exclu=[]

for directory in os.listdir(data_src):
    print(directory)
    temp=[]
    c=0

    for pic in os.listdir(os.path.join(data_src, directory)):
        img = cv2.imread(os.path.join(data_src, directory, pic))
        img = cv2.resize(img, (224,224))

        temp.append(np.squeeze(np.asarray(img)))

        X.append(np.squeeze(np.asarray(img)))
        y.append(directory)
        id.append(c)
        c=c+1
    direcX.append(np.array(temp))
    direcy.append(directory)

    print(len(direcX),len(temp))
    ss=np.squeeze(np.asarray(computefeat(temp,direcX[k])))
    print(ss)
    print(len(direcX[k]),len(temp))

    k=k+1
    with open(save_dir+directory+'.pkl','wb') as f:
        pickle.dump(ss, f)
    F.append(ss)
    

print('Dataset loaded successfully.')
