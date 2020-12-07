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
from random import randint

cv2.ocl.setUseOpenCL(False)

# data_src= '/home/kuru/Desktop/adiusb/veri-split/veriN_fol/image_train/'
# data_src_out='/home/kuru/Desktop/adiusb/veri-split/veriN/image_train'


data_src= '/home/kuru/Desktop/market_noise/image_train/'
data_src_out='/home/kuru/Desktop/market_noiseall/image_train'

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
for directory in os.listdir(data_src):
    #print(directory)

    c=0

    for pic in os.listdir(os.path.join(data_src, directory)):
        #print(pic)
        img = cv2.imread(os.path.join(data_src, directory, pic))
        #img = cv2.resize(img, (224,224))
        aa=(pic.split('.'))
        pic=(aa[0]+'.jpg')
        gg=(pic.split('_'))
        if(gg[1]=='c10s10'):
            gg[1]='c3s3'
            gg[2]=str('0'+str(randint(10000,99999)))

        pic=gg[0]+'_'+gg[1]+'_'+gg[2]+'_'+gg[3]

        # if(str(aa[0])=='jpeg'):
        #     print(aa)
        #     pic=str( aa[0] +'.'+ aa[1])
        #     print(pic)
        name.append(str(pic))
        pathout=data_src_out + '/'+ (str(pic))
        print(pathout)
        #cv2.imwrite(pathout, img) 
