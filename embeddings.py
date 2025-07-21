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

# Create the query vector from query_text
query_text = "computer"
query_vector = create_embeddings(query_text)[0]

# Find the five closest distances
hits = find_n_closest(query_vector, product_embeddings, n=5)

print(f'Search results for "{query_text}"')
for hit in hits:
  # Extract the product at each index in hits
  product = products[hit['index']]
  print(product["title"])

  # Combine the features for last_product and each product in products
last_product_text = create_product_text(last_product)
product_texts = [create_product_text(product) for product in products]

# Embed last_product_text and product_texts
last_product_embeddings = create_embeddings(last_product_text)[0]
product_embeddings = create_embeddings(product_texts)[0]

# Find the three smallest cosine distances and their indexes
hits = find_n_closest(last_product_embeddings, product_embeddings)

for hit in hits:
  product = products[hit['index']]
  print(product['title'])


 # Prepare and embed the user_history, and calculate the mean embeddings
history_texts = [create_product_text(article) for article in user_history]
history_embeddings = create_embeddings(history_texts)[0]
mean_history_embeddings = np.mean(history_embeddings, axis=0)

# Filter products to remove any in user_history
products_filtered = [product for product in products if product not in user_history]

# Combine product features and embed the resulting texts
product_texts = [create_product_text(product) for product in products_filtered]
product_embeddings = create_embeddings(product_texts)[0]

hits = find_n_closest(mean_history_embeddings, product_embeddings)

for hit in hits:
  product = products_filtered[hit['index']]
  print(product['title']) 


# Define a function to return the minimum distance and its index
def find_closest(query_vector, embeddings):
  distances = []
  for index, embedding in enumerate(embeddings):
    dist = distance.cosine(query_vector, embedding)
    distances.append({"distance": dist, "index": index})
  return min(distances, key=lambda x: x["distance"])

for index, review in enumerate(reviews):
  # Find the closest distance and its index using find_closest()
  closest =find_closest(review_embeddings[index], class_embeddings)
  label = sentiments[closest['index']]['label']
  print(f'"{review}" was classified as {label}')