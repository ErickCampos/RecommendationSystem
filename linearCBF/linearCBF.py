import numpy as np
import pandas as pd
import time

def linearCBF(lr, reg, miter):
    mat = np.load('../fm/meanTrain.npy') 
    dados = pd.read_csv('../data/train.csv')
    dados = pd.read_csv('../data/train.csv')
    nUsers = 3974
    nItens = 3564
    m = 19
    bias = np.zeros((3564,1))
    bias[:] = 1
    features = np.load('features.npy')
    features = np.append(features, bias, axis=1)
    profiles = np.random.normal(loc=0, scale=0.1, size=(nUsers, m))
    error = []

    for l in range(0,miter):
        sq_error = 0
        for j in dados.index:
            u = dados['user_id'][j]-1
            i = dados['movie_id'][j]-1
            r = dados['rating'][j]
            e = np.dot(profiles[u,:],features[i,:]) - r
            sq_error += np.power(e,2)
            for k in range(0,18):
                profiles[u,k] = profiles[u,k] - lr * (e * features[i,k] + reg * profiles[u,k])
            
            profiles[u,m-1] = profiles[u,m-1] - lr * (e * features[i,m-1])            

        rmse = np.sqrt(sq_error/len(dados.index))
        error.append(rmse)
        print('RMSE: ', rmse)
    np.save('profiles.npy',profiles)
    np.save('features.npy',features)
    print('Train model saved')

if __name__=='__main__':
    start_time = time.time()
    linearCBF(0.05, 0.002, 10)
    print('Train time:  ', time.time()-start_time)
