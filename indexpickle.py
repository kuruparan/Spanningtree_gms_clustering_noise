import os
import pickle
#src = '/home/kuru/Desktop/adiusb/veri-split/noise776_outrm/'
src ='/home/kuru/Desktop/market_noise/image_train/'
index = {}
for directory in os.listdir(src):
    s = directory
    count = 0
    path1 = src+directory+'/'
    for pic in os.listdir(path1):
        index[pic] = (pic[1:4], count)
        count = count+1
print(index)        
print(len(index))
with open('index_market_noise.pkl', 'wb') as handle:
    b = pickle.dump(index, handle, protocol=pickle.HIGHEST_PROTOCOL)