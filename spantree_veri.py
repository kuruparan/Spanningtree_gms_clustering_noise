import os
import pickle
pkl = {}
k=[]
path = '/home/kuru/Desktop/veri-gms-master/gms/'
entries = os.listdir(path)
for name in entries:
    f = open((path+name), 'rb')
    ccc=(path+name)
    #print(ccc)
    if name=='featureMatrix.pkl':
        s = name[0:13]
        #print(s)
        
    else:
        s = name[0:3]
        #print(s)
        k.append(s)
       
    #print(s)
    #with open (ccc,"rb") as ff:
    #    pkl[s] = pickle.load(ff)
        #print(pkl[s])
    pkl[s] = pickle.load(f)
    f.close
#print(len(pkl))
#print(k)
print(pkl[k[0]])
#print(list(pkl)[0:5])

#X=pkl[k[0]]

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
X = csr_matrix([[0, 8, 0, 3],
                [0, 0, 2, 5],
                [0, 0, 0, 6],
                [0, 0, 0, 0]])
Tcsr = minimum_spanning_tree(X)
Tcsr.toarray().astype(int)
print(Tcsr)