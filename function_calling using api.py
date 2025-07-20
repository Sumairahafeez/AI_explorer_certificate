from openai import OpenAI

# function definitions
function_definition[0]['function']['paramteres']['type'] = 'object'
function_definition[0]['function']['parameters']['properties'] = {
    'title': {'type': 'string', 'description': 'The title of the book'},
    'author': {'type': 'string', 'description': 'The author of the book'},
    'year': {'type': 'integer', 'description': 'The year the book was published'},
}

# get response 
def get_response(prompt, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=100,
        tools=function_definition,
        function_call={"name": "get_book_info"}
    )
    return response.choices[0].message.content

# get answer
response = get_response("What is the title of the book 'To Kill a Mockingbird'?")
print(response.choices[0].message.tools[0].function.arguments)
