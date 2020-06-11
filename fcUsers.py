import numpy as np
import pandas as pd
import math

def pred(user,item,k):
    mat = np.load('train.npy')
    u = []#user test 
    v = []#user train 
    sim = []
    #calculating similarity
    for i in range(0, 3974):
        sum1 = 0
        sum2 = 0
        result = 0
        if i == user or math.isnan(mat[i][item]):
            continue
        uBias = np.nanmean(mat[user,:])#user test
        vBias = np.nanmean(mat[i,:])#user train
        if math.isnan(uBias):
            uBias = 0
        if math.isnan(vBias):
            vBias = 0
        for j in range(0,3564):
            if math.isnan(mat[user][j]) or math.isnan(mat[i][j]):
                continue
            else:
                u.append(mat[user][j])#user test
                v.append(mat[i][j])#user train
        if len(u) == 0:
            sim.append((0,i))
        for x in range(0, len(u)):
            sum1 += (u[x]-uBias) * (v[x]-vBias)
            sum2 += np.sqrt(np.power((u[x]-uBias),2)) * np.sqrt(np.power((v[x]-vBias),2))
        result = sum1/sum2 #similarity
        if math.isnan(result):
            sim.append((0,i))
        else:
            #print(result)
            sim.append((result,i))
        u.clear()
        v.clear()
    sim = sorted(sim, key=lambda tup: tup[0])
    sum1 = 0
    sum2 = 0
    pred = 0
    for y in range(0,k):
        vUser = sim[x][1] 
        sum1 += sim[x][0] * mat[vUser][item]
        sum2 += sim[x][0]
    pred = uBias + sum1/sum2
    sim.clear()
    return pred

if __name__=='__main__':
    test = pd.read_csv('data/train.csv')
    for ind in test.index:
        user = test['user_id'][ind]-1
        item = test['movie_id'][ind]-1
        nada = pred(user,item,10)
        print(nada)
