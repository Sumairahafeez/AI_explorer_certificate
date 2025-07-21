# first import pinecone
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()
# Initialize Pinecone
pinecone = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"))