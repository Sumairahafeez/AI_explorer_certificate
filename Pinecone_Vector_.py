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