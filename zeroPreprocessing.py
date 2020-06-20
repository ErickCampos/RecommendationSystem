import numpy as np
import pandas as pd


dados = pd.read_csv('data/train.csv')
arr = np.zeros((3974,3564))

for ind in dados.index:
    user = dados['user_id'][ind]
    movie = dados['movie_id'][ind]
    rating = dados['rating'][ind]
    arr[user-1][movie-1] = rating

np.save('zeroTrain.npy',arr)
