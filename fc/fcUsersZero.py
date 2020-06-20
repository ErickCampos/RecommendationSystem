import numpy as np
import pandas as pd
from sklearn.metrics import pairwise_distances
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

def calSimilarity():
    mat = np.load('../zeroTrain.npy')
    sparseMat = sparse.csr_matrix(mat)
    similarities = cosine_similarity(sparseMat)
    return similarities

def predict(sim,user,item,k):
    mat = np.load('../zeroTrain.npy')
    sum1 = 0
    sum2 = 0
    uBias = np.mean(mat[user,:])
    sim = sorted(sim, key=lambda tup: tup[0], reverse=True) 
    for i in range(0,k):
        vUser = sim[i][1]
        vBias = np.mean(mat[vUser,:])
        sum1 += sim[i][0] * (mat[vUser][item] - vBias)
        sum2 += sim[i][0]
    if sum2 == 0:
        pred = 0
    else:
        pred = uBias + sum1/sum2
    pred = round(pred,2)
    if pred < 0:
        pred = np.abs(0)
    print(pred)


if __name__=='__main__':
    similarities = calSimilarity()
    test = pd.read_csv('../data/test.csv')
    sim = []
    for ind in test.index:
        user = test['user_id'][ind]-1
        item = test['movie_id'][ind]-1
        temp = similarities[user,:]
        for i in range(0,len(temp)):
            if i == user:
                continue
            sim.append((temp[i],i))
        predict(sim,user,item,200)
        sim.clear()
