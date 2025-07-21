# Start coding here
# Use as many cells as you need.
client = openai.OpenAI()
def create_embeddings(text):
    client.embeddings.create(
        model = 'text-small-model',
        input = text
    )
    return client.model_dump()
response = create_embeddings(review_text)   
embeddings = [response["embedding"] for response in responses['data']]
def apply_tsne(embeddings):
    tsne = TSNE(n_components = 2, random_state = 0)
    return tsne.fit_transform(embeddings)
embeddings_2d = apply_tsne(embeddings)
def plot_tsne(tsne_results):
    plt.figure(figsize=(12,8))
    for i,point in enumerate(tsne_results):
       plt.scatter(point[0], point[1], alpha=0.5)
       plt.text(point[0], point[1], str(i), fontsize=8, verticalalignment='center')
    plt.title("t-SNE Visualization of Review Embeddings")
    plt.xlabel("t-SNE feature 1")
    plt.ylabel("t-SNE feature 2")
    plt.show()
plot_tsne(embeddings_2d)
categories = ['Quality','Fit','Style','Comfort']
category_responses = create_embeddings(categories)
category_embeddings = [embedding['embedding'] for embedding in category_responses['data']]

def categorize_feedback(text_embedding,category_embedding):
    similarities = [{"distance": distance.cosine(text_embedding,cat_emb), "index":i} for i,cat_emb in enumerate(category_embedding)]
    closest = min(similarities,key = lambda x:x['index'])
    return categories[closest['index']]
# Categorize feedback
feedback_categories = [categorize_feedback(embedding, category_embeddings) for embedding in embeddings]


# Initialize Chromadb instance for vector storage
client = chromadb.PersistentClient()

# Define vector database
review_embeddings_db = client.create_collection(
    name="review_embeddings",
    embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key=os.environ["OPENAI_API_KEY"]))

# Store embeddings inside vector database
review_embeddings_db.add(
    documents=review_texts.tolist(),
    ids=[str(i) for i in range(len(review_texts))]
)

# Function for similarity search using vector db query function
def find_similar_reviews(input_text, vector_db, n=3):
    collection = client.get_collection(
        name="review_embeddings",
        embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key=os.environ["OPENAI_API_KEY"]))
    results = collection.query(
        query_texts=[input_text],
        n_results=n
    )
    return results

# Example feedback and finding similar feedback
example_review = "Absolutely wonderful - silky and sexy and comfortable"
most_similar_reviews = find_similar_reviews(example_review, review_embeddings_db, 3)["documents"][0]
print(most_similar_reviews)

# Clean up
client.delete_collection(name="review_embeddings")
    
    