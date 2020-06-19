import numpy as np
import pandas as pd

def funkSVD(mat, data, k, lr, reg, miter):
    globalMean = np.nanmean(mat)
    nUsers = 3974
    nItens = 3564
    bu = np.zeros(nUsers)
    bi = np.zeros(nItens)
    p = np.full((nUsers,k),0.1)
    q = np.full((nUsers,k),0.1)

    for f in range(0,k):
        for l in range(0,miter):
            for ind in data.index:
                u = dados['user_id'][ind]-1                                                
                i = dados['movie_id'][ind]-1                                             
                r = dados['rating'][ind]
                pred = globalMean + bu[u] + bi[i]  
    return 1

if __name__=='__main__':
    mat = np.load('../train.npy')
    dados = pd.read_csv('../data/train.csv')
    nada = funkSVD(mat,dados,20,0.05,0.02,10)
    print(nada)
