import numpy as np
import pandas as pd
import time

def predict(user,item):
    features = np.load('feat.npy')
    profiles = np.load('profiles.npy')
    pred = np.dot(profiles[user,:], features[item,:])
    if pred < 0.0:
        pred = abs(pred)
    print(round(pred,2))


if __name__=='__main__':
    test = pd.read_csv('../data/test.csv')                                      
    print('id,rating')
    cont = 0
    for ind in test.index:                                                      
        user = test['user_id'][ind]-1                                           
        item = test['movie_id'][ind]-1                                                                                                            
        print(cont, end=',')
        predict(user,item)
        cont += 1
