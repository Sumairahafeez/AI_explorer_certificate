import json
from openai import OpenAI
import pandas as pd

# extracting data 
df = pd.read_csv("transcriptions.csv")
df.head()
# initializing openai key
client = OpenAI()

# defining function to extract age and recommend treatment
def extract_info_with_openai(transcription):
    messages = [
        {
            'role':'system',
            'content':'you are a medical assistant chatbot that provides information and treatment using the provided dataset'
            'role':'user',
            'content':'please extract both the patients age and treatment from the given transcription : {transcription}'
        }
    ]
    function_definition = [
        'type': 'function',
        'function': {
            'name':'extract_medical_data',
            'decription':'get patients age and recommended treatment from the given transcript',
            'parameters': {
                'type':'object',
                'properties': {
                    'age' : {
                        'type' :"integer",
                        'description' : "age of the patient"
                    }
                    'recommended_treatment' : {
                        'type' :"string"
                        'description':"recommened treatment for the patient"
                    }
                }
            }
        }
    ]
    response = client.chat.completion.create(
        model = 'gpt-4o-mini',
        messages = messages,
        tools_call = function_definition
    )
    return json.loads(response.choices[0].message.tools_call[0].function.arguments)
def get_icd_codes(treatment):
    if treatment != 'Unknown':
        response = client.chat.completion.create(
            model='gpt-4o-mini',
            messages=[
                {
                    'role': 'system',
                    'content': 'You are a medical coding assistant that provides ICD codes for treatments.'
                },
                {
                    'role': 'user',
                    'content': f'Please provide the ICD code for the following treatment: {treatment}'
                }
            ]
        )
        return response.choices[0].message.content.strip()
    return 'Unknown'
processed_data = []
for transcription in df['transcription']:
    extracted_info = extract_info_with_openai(transcription)
    age = extracted_info.get('age', 'Unknown')
    treatment = extracted_info.get('recommended_treatment', 'Unknown')
    icd_code = get_icd_codes(treatment)
    
    processed_data.append({
        'transcription': transcription,
        'age': age,
        'recommended_treatment': treatment,
        'icd_code': icd_code
    })
# Creating a DataFrame from the processed data
processed_df = pd.DataFrame(processed_data)