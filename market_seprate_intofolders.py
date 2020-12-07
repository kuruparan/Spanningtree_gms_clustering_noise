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

# data_src= '/home/kuru/Desktop/duke/DukeMTMC-reID/image_test/'
# data_src_out='/home/kuru/Desktop/duke_fol/image_test'


data_src_out= '/home/kuru/Desktop/market_noise/image_train'
data_src='/home/kuru/Desktop/market_noiseall/image_train/'


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
for pic in os.listdir(data_src):
    #print(directory)

    c=0


    #print(pic)
    img = cv2.imread(os.path.join(data_src, pic))
    #img = cv2.resize(img, (224,224))
    directory= int(str(pic).split('_')[0])
    #print(directory)
    name.append(str(pic))
    my_folder=data_src_out + '/'+ str(directory)
    if not os.path.exists(my_folder):
        os.makedirs(my_folder)
    pathout=data_src_out + '/'+ str(directory)+'/'+ (str(pic))
    #print(pathout)

    cv2.imwrite(pathout, img) 
