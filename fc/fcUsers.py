import numpy as np
import pandas as pd
import math

def pred(user,item,k):
    mat = np.load('../train.npy')
    u = []#user test 
    v = []#user train 
    sim = []
    #calculating similarity
    for i in range(0, 3974):
        sum1 = 0
        sum2 = 0
        sumU = 0
        sumV = 0
        result = 0
        uBias = 0
        vBias = 0
        if i == user or math.isnan(mat[i][item]):
            continue
        uBias = np.nanmean(mat[user,:])#user test
        vBias = np.nanmean(mat[i,:])#user train
        if math.isnan(uBias):
            #print('uBias is NaN')
            return
        if math.isnan(vBias):
            #print('vBias is NaN')
            continue
        for j in range(0,3564):
            if math.isnan(mat[user][j]) or math.isnan(mat[i][j]):
                continue
            else:
                u.append(mat[user][j])#user test
                v.append(mat[i][j])#user train
        if len(u) == 0:
            continue
        for x in range(0, len(u)):
            sum1 += (u[x]-uBias) * (v[x]-vBias)
            sumU += np.power((u[x]-uBias),2)
            sumV += np.power((v[x]-vBias),2)
            sum1 = round(sum1,4) 
            sumU = round(sumU,4) 
            sumV = round(sumV,4) 
        result = sum1/(np.sqrt(sumU) * np.sqrt(sumV))#similarity
        result = round(result,4)
        if math.isnan(result):
            continue
        else:
            sim.append((result,i))
        u.clear()
        v.clear()
    sim = sorted(sim, key=lambda tup: tup[0], reverse=True)
    sum1 = 0
    sum2 = 0
    pred = 0
    if k > len(sim):
        k = len(sim)
    for y in range(0,k):
        vUser = sim[y][1] 
        sum1 += sim[y][0] * (mat[vUser][item] - vBias)
        sum2 += sim[y][0]
        sum1 = round(sum1,4)
        sum2 = round(sum2,4)
    sim.clear()
    if sum2 == 0:
        print('Erro', end=' ')
        print(sum2)
        return
    pred = uBias + sum1/sum2
    pred = round(pred,4)
    print(pred)

if __name__=='__main__':
    test = pd.read_csv('../data/test.csv')
    for ind in test.index:
        user = test['user_id'][ind]-1
        item = test['movie_id'][ind]-1
        pred(user,item,5)
