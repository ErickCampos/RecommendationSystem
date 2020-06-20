import numpy as np
import pandas as pd
import math 
from scipy.sparse.linalg import svds
import time
import sys

def pred(u,sigma,v,user,item):
    p = u[user,:]
    q = v[item,:]
    rating = 0
    for i in range(0,len(q)):
        rating += p[i]*sigma[i]*q[i]
    rating = round(rating,2)
    if rating > 5.0:
        rating = 5.0
    print(rating)

if __name__=='__main__':
    k = sys.argv[1]
    test = pd.read_csv('../data/test.csv')
    mat = np.load('meanTrain.npy')
    start_time = time.time()
    u, s, v = svds(mat,int(k))
    print('id,rating')
    cont = 0
    for ind in test.index:                                                      
        user = test['user_id'][ind]-1                                           
        item = test['movie_id'][ind]-1                                          
        print(cont,end=',')
        pred(u,s,v.transpose(),user,item)
        cont += 1
    arquivo = open('NaN.txt','a') # Abra o arquivo (leitura)
    arquivo.write(str(time.time() - start_time))
    arquivo.write('\n')
    arquivo.close()
