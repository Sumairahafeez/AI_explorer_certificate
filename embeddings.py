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