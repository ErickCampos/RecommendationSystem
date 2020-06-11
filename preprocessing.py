import numpy as np
import pandas as pd


dados = pd.read_csv('data/train.csv')
arr = np.empty((3974,3564))
arr[:] = np.NaN

for ind in dados.index:
    user = dados['user_id'][ind]
    movie = dados['movie_id'][ind]
    rating = dados['rating'][ind]
    arr[user-1][movie-1] = rating
    #arr[dados['user_id'][ind]]-1,dados['movie_id'][ind]-1] = dados['rating'][ind]]-1

np.save('train.npy',arr)
