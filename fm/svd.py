import numpy as np
import pandas as pd
import math 
from scipy.sparse.linalg import svds
import time

def replaceNaN():
    mat = np.load('../train.npy')
    for i in range(0,3974):
        mean = np.nanmean(mat[i,:])
        for j in range(0,3564):
            if math.isnan(mat[i][j]):
                if math.isnan(mean):
                    mean = np.nanmean(mat[:,j])
                if math.isnan(mean):
                    mean = 0
                mat[i][j] = mean
    return mat

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
    #start_time = time.time()
    test = pd.read_csv('../data/test.csv')
    mat = replaceNaN()
    u, s, v = svds(mat, k=5)
    for ind in test.index:                                                      
        user = test['user_id'][ind]-1                                           
        item = test['movie_id'][ind]-1                                          
        pred(u,s,v.transpose(),user,item)
    #print(time.time() - start_time)
