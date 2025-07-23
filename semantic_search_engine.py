import pinecone
import os
from pinecone import Pinecone, ServerlessSpec
import dotenv
dotenv.load_dotenv()
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

# Create Pinecone index
pc.create_index(
    name='pinecone-datacamp', 
    dimension=1536,
    spec=ServerlessSpec(cloud='aws', region='us-east-1')
)

# Connect to index and print the index statistics
index = pc.Index('pinecone-datacamp')
print(index.describe_index_stats())

batch_limit = 100

for batch in np.array_split(df, len(df) / batch_limit):
    # Extract the metadata from each row
    metadatas = [{
      "text_id": row['id'],
      "text": row['text'],
      "title": row['title']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Encode texts using OpenAI
    response = client.embedding.crate(input=texts, model="text-embedding-3-small")
    embeds = [np.array(x.embedding) for x in response.data]
    
    # Upsert vectors to the correct namespace
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace='squad_dataset')
query = "What is in front of the Notre Dame Main Building?"

# Create the query vector
query_response = client.embeddings.create(
    input=query,
    model="text-embedding-3-small"
)
query_emb = query_response.data[0].embedding

# Query the index and retrieve the top five most similar vectors
retrieved_docs = index.query(
    vector=query_emb,
    top_k=5,
    namespace = 'squad_dataset'
)

for result in retrieved_docs['matches']:
    print(f"{result['metadata']['title']}: {result['metadata']['text']}")    