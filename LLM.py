# Import the class for defining Hugging Face pipelines
from langchain_huggingface import HuggingFacePipeline

# Define the LLM from the Hugging Face model ID
llm = HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20}
)

prompt = "Hugging Face is"

# Invoke the model
response = llm.invoke(prompt)
print(response)

from langgraph.prebuilt import create_react_agent 
from langchain_community.agent_toolkits.load_tools import load_tools
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
tools = load_tools(["llm-math"], llm=llm)
agent = create_react_agent(llm, tools)
messages = agent.invoke({"messages": [("human", "What is the square root of 101?")]})
print(messages)