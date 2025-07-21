from openai import OpenAIEmbeddings
import json

products_description = [product['short_description']for product in products]
client = OpenAIEmbeddings()
response = client.embeding.create(
    model='text-embedding-3-small',
    input=products_description
)
response_Dict = response.model_dump()

for i, product in enumerate(products):
    products['embedding'] = response_Dict['data'][i]['embedding']

# working is t-sne
from scikit.manifold import TSNE
import pandas as pd
import numpy as np

embeddings = np.array([product['embedding'] for product in products])
categories = [product['category'] for product in products]
tsne = TSNE(n_components=2, perplexity=4)
embeddings_2d = tsne.fit_transform(embeddings)
matplotlib.pyplot.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], c=categories, cmap='viridis')
pyplot.show()
# measuring similarity between vectors using cosine function
# creating a function to calculate cosine similarity

def create_embeddings(text):
    client = OpenAIEmbeddings()
    response = client.embeding.create(
        model='text-embedding-3-small',
        input=text
    )
    return response.model_dump()['data'][0]['embedding']

search_text = "soap"
search_embedding = create_embeddings(search_text)
distance = []
for product in products:
    product['similarity'] = cosine_similarity(search_embedding, product['embedding'])
    distance.append(product['similarity'])
min_distance = min(distance)
most_similar_product = products[distance.index(min_distance)]
# now there are three steps for finding the most similar product:
# 1. Create embeddings for the search text.
# 2. Calculate cosine similarity between the search embedding and each product's embedding.
# 3. Find the product with the highest similarity score.

def create_embeddings(text):
    client = OpenAIEmbeddings()
    response = client.embeding.create(
        model='text-embedding-3-small',
        input=text
    )
    return response.model_dump()['data'][0]['embedding']

def find_n_closest(query_vector, embeddings, n=3):
  distances = []
  for index, embedding in enumerate(embeddings):
    # Calculate the cosine distance between the query vector and embedding
    dist = distance.cosine(query_vector,embedding)
    # Append the distance and index to distances
    distances.append({"distance": dist, "index": index})
  # Sort distances by the distance key
  distances_sorted = sorted(distances, key = lambda x:x["distance"])
  # Return the first n elements in distances_sorted
  return distances_sorted[0:n]