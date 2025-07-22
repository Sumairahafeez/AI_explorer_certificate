# first import pinecone
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()
# Initialize Pinecone
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"))
# Create your Pinecone index
# Create your Pinecone index
pc.create_index(
    name="my-first-index",
    dimension=256,
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)
# describing index stats
index = pc.Index("my-first-index")
index.describe_index_stats()
pc.delete_index("my-first-index")
pc.list_indexes()

# Create your Pinecone index
pc.create_index(
    name="datacamp-index", 
    dimension=1536, 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'
    )
)
vectors = [
    {
        "id": "vec1",
        "values": [0.1] * 1536
    },
    {
        "id": "vec2",
        "values": [0.2] * 1536
    }
]
# Check that each vector has a dimensionality of 1536
vector_dims = [len(vector['values']) == 1536 for vector in vectors]
print(pc.describe_index_stats(vector_dims))

# upserting vectors
# Connect to your index
index = pc.Index("datacamp-index")

# Ingest the vectors and metadata
index.upsert(
    vectors = vectors
)

# Print the index statistics
print(index.describe_index_stats())

index = pc.Index('datacamp-index')
ids = ['2', '5', '8']

# Fetch vectors from the connected Pinecone index
fetched_vectors = index.fetch(ids=ids)

# Extract the metadata from each result in fetched_vectors
metadatas = [fetched_vectors['vectors'][id]['metadata'] for id in ids]
print(metadatas)

def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    # Convert the iterable into an iterator
    it = iter(iterable)
    # Slice the iterator into chunks of size batch_size
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        # Yield the chunk
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))
index = pc.Index('datacamp-index')

# Upsert vectors in batches of 100
for chunk in chunks(vectors):
    index.upsert(vectors=chunk)


# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())        