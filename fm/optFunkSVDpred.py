import numpy as np
import pandas as pd
import time 


def predict(user,item,globalMean,bu,bi,p,q):
    pred = globalMean + bu[user] + bi[item] + np.dot(p[user,:],q[item,:])
    if pred > 5.0:
        pred = 5.0
    pred = round(pred,1)
    print(pred)

if __name__=='__main__':
    start_time = time.time()
    mat = np.load('../train.npy')
    globalMean = np.nanmean(mat)
    bu = np.load('bu.npy')
    bi = np.load('bi.npy')
    p = np.load('p.npy')
    q = np.load('q.npy')
    test = pd.read_csv('../data/test.csv')
    print('id,rating')
    cont=0
    for ind in test.index:
        user = test['user_id'][ind]-1
        item = test['movie_id'][ind]-1
        print(cont,end=',')
        predict(user,item,globalMean,bu,bi,p,q)        
        cont+=1
    print('Tempo:  ', time.time()-start_time)
