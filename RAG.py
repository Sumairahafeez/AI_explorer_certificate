from openai import OpenAI
import numpy as np
import dotenv
from uuid import uuid4
from pinecone import Pinecone, ServerlessSpec
import os
import pandas as pd
dotenv.load_dotenv()
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
youtube_df = pd.read_csv('youtube_data.csv')  # Assuming you have a DataFrame with YouTube data
client = OpenAI()


index = pc.Index('pinecone-datacamp')

batch_limit = 100

for batch in np.array_split(youtube_df, len(youtube_df) / batch_limit):
    # Extract the metadata from each row
    metadatas = [{
      "text_id": row['id'],
      "text": row['text'],
      "title": row['title'],
      "url": row['url'],
      "published": row['published']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Encode texts using OpenAI
    response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    embeds = [np.array(x.embedding) for x in response.data]
    
    # Upsert vectors to the correct namespace
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace='youtube_rag_dataset')
    
print(index.describe_index_stats())

def retrieve(query, top_k, namespace, emb_model):
    # Encode the input query using OpenAI
    query_response = client.embeddings.create(
        input= query,
        model=emb_model
    )
    
    query_emb = query_response.data[0].embedding
    
    # Query the index using the query_emb
    docs = index.query(vector=query_emb, top_k=top_k, namespace=namespace, include_metadata=True)
    
    retrieved_docs = []
    sources = []
    for doc in docs['matches']:
        retrieved_docs.append(doc['metadata']['text'])
        sources.append((doc['metadata']['title'], doc['metadata']['url']))
    
    return retrieved_docs, sources

documents, sources = retrieve(
  query="How to build next-level Q&A with OpenAI",
  top_k=3,
  namespace='youtube_rag_dataset',
  emb_model="text-embedding-3-small"
)
print(documents)
print(sources)