import os
import openai
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

openai.api_key = os.environ.get("OPENAI_API_KEY")

template = """Conversation with GPT API
{history}
Human: {human_input}
Assistant:"""

prompt = PromptTemplate(
    input_variables=["history", "human_input"], 
    template=template
)


chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0), 
    prompt=prompt, 
    verbose=True, 
    memory=ConversationBufferWindowMemory(k=2),
)

while True:
    message = input("Please enter a message or type 'exit' to quit: ")

    if message.lower() == "exit":
        break

    output = chatgpt_chain.predict(human_input=message)
    print(output)
    
