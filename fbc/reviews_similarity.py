import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics.pairwise import cosine_similarity
import time

start_time = time.time()
mat = list()
for i in range(0, 3564):
    mat.append('')

df = pd.read_csv('../data/movie_reviews.csv')
for row in df.itertuples():
    movie = getattr(row, 'movie_id')-1
    text = getattr(row, 'text')
    mat[movie] += str(text)



tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')
matrix = tf.fit_transform([review for index, review in enumerate(mat)])
print('Similaridades...')
similarities = cosine_similarity(matrix)
np.save('fbc_sim.npy',similarities)
print(similarities.shape)
print(time.time()-start_time)
