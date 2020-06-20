import numpy as np
import pandas as pd
from sklearn.metrics import pairwise_distances
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

def calSimilarity():
    data = np.load('../zeroTrain.npy')
    mat = data.transpose()
    sparseMat = sparse.csr_matrix(mat)
    similarities = cosine_similarity(sparseMat)
    return similarities

def predict(sim,user,item,k):
    mat = np.load('../zeroTrain.npy')
    sum1 = 0
    sum2 = 0
    sim = sorted(sim, key=lambda tup: tup[0], reverse=True) 
    for i in range(0,k):
        jItem = sim[i][1]
        sum1 += sim[i][0] * mat[user][jItem]
        sum2 += sim[i][0]
    if sum2 == 0:
        pred = 0
    else:
        pred = sum1/sum2
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
        temp = similarities[item,:]
        for j in range(0,len(temp)):
            if j == item:
                continue
            sim.append((temp[j],j))
        predict(sim,user,item,10)
        sim.clear()
