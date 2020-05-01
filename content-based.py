#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import sys
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
book_description = pd.read_csv('description.csv', encoding = 'latin-1')
books_tfidf = TfidfVectorizer(stop_words='english')
book_description['description'] = book_description['description'].fillna('')
book_description_matrix = books_tfidf.fit_transform(book_description['description'])
cosine_similarity = linear_kernel(book_description_matrix, book_description_matrix)
indices = pd.Series(book_description['name'].index)
def recommend(index, cosine_sim=cosine_similarity):
    id = indices[index]
    similarity_scores = list(enumerate(cosine_sim[id]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:6]
    books_index = [i[0] for i in similarity_scores]
    return book_description['name'].iloc[books_index]
k=recommend(int(sys.argv[1]))
k=k.to_json()
for i in k:
	print(i)