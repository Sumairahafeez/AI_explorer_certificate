# chroma DB is used for vector databases for storing and querying embeddings
import chromadb

# Retrieve the netflix_titles collection
collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

# Query the collection for "films about dogs"
result = collection.query(
  query_texts = ["films about dogs"],
  n_results = 3)

print(result)

collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

# Update or add the new documents
collection.add(
    ids= [doc['id'] for doc in new_data],
    documents=[doc['document'] for doc in new_data]
)

# Delete the item with ID "s95"
collection.delete(
  ids = 's95'
)
result = collection.query(
    query_texts=["films about dogs"],
    n_results=3
)
print(result)

collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

reference_ids = ['s999', 's1000']

# Retrieve the documents for the reference_ids
reference_texts = collection.get(ids = reference_ids)['documents']

# Query using reference_texts
result = collection.query(
  query_texts = reference_texts,
  n_results = 3
)

print(result['documents'])