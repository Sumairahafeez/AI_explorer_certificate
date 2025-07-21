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

