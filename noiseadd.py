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
from random import randrange
import random

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

data_src= '/home/kuru/Desktop/adiusb/veri-split/veriNoise50/'
data_src_ori= '/home/kuru/Desktop/adiusb/veri-split/noise/'
data_src_out= '/home/kuru/Desktop/adiusb/veri-split/noise50out/'

save_dir = './gms/'
X = []
y = []
direcX=[]
direcy=[]
F=[]
id=[]
k=0
exclu=[]

allnoise=[]
name=[]
for directory in os.listdir(data_src_ori):
    #print(directory)

    c=0

    for pic in os.listdir(os.path.join(data_src_ori, directory)):
        #print(pic)
        img = cv2.imread(os.path.join(data_src, directory, pic))
        #img = cv2.resize(img, (224,224))
        name.append(str(pic))
        allnoise.append(np.squeeze(np.asarray(img)))

print(len(allnoise))

for directory in os.listdir(data_src):
    print(directory)
    #print(len(os.listdir(os.path.join(data_src, directory))))
    noise_count=round(len(os.listdir(os.path.join(data_src, directory)))/3)
    random_index= random.sample(range(0, len(allnoise)-1), noise_count)
    #print(random_index)
    for k in random_index:
        #print(name[k])
        change=str(name[k])
        changel=list(change)
        #print(changel)
        dir_in0=changel[1:4]
        dir_in=''.join(dir_in0)

        changel[1:4]=list(str(directory))
        change= ''.join(changel)
        #print(change)
        pathin=data_src_ori+ str(dir_in)+'/'+ name[k]
        pathout=data_src_out+ str(directory)+'/'+ change
        #path2=os.path.join(data_src_out, str(directory),'/', change, '.jpg')
        print(pathin,pathout)
        img=cv2.imread(pathin)
        #print(img)
        cv2.imwrite(pathout, img) 
        #break
    #break



    # for pic in os.listdir(os.path.join(data_src, directory)):
    #     print(pic)
    #     img = cv2.imread(os.path.join(data_src, directory, pic))
    #     #img = cv2.resize(img, (224,224))
    #     name.append(str(pic))
    #     allnoise.append(np.squeeze(np.asarray(img)))



    # for directory in os.listdir(data_src):
    #     print(directory)

    # temp=[]
    # c=0

    # for pic in os.listdir(os.path.join(data_src, directory)):
    #     img = cv2.imread(os.path.join(data_src, directory, pic))
    #     img = cv2.resize(img, (224,224))

    #     temp.append(np.squeeze(np.asarray(img)))

    #     X.append(np.squeeze(np.asarray(img)))
    #     y.append(directory)
    #     id.append(c)
    #     c=c+1
    # direcX.append(np.array(temp))
    # direcy.append(directory)

    # print(len(direcX),len(temp))
    # ss=np.squeeze(np.asarray(computefeat(temp,direcX[k])))
    # print(ss)
    # print(len(direcX[k]),len(temp))

    # k=k+1
    # with open(save_dir+directory+'.pkl','wb') as f:
    #     pickle.dump(ss, f)
    # F.append(ss)
    

print('Dataset loaded successfully.')
