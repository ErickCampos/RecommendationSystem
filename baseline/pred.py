import numpy as np
import pandas as pd

def pred(user,item,mean):
    movieBaseline = np.load('movieBaseline.npy')
    userBaseline = np.load('userBaseline.npy')
    result = mean + movieBaseline[item] + userBaseline[user]
    result = round(result,2)
    print(result)

if __name__=='__main__':
    test = pd.read_csv('../data/test.csv')
    mat = np.load('../train.npy')
    mean = np.nanmean(mat)
    for ind in test.index:
        user = test['user_id'][ind]-1
        item = test['movie_id'][ind]-1
        pred(user,item,mean)
