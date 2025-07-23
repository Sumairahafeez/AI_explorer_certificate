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