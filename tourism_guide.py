# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Start coding here
# Add as many cells as you like
conversations = [{"role": "system", "content": "You are a tourist chatbot assisting tourists and their activities"}]
questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]

def get_response(prompt):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=100
    )
    return response.choices[0].message.content

for q in questions:
    print(q)
    input_dict = {'role': 'user', 'content': q}
    result = get_response(q)
    output_dict = {'role': 'assistant', 'content': result}
    conversations.append(input_dict)
    conversations.append(output_dict)
    print(result)