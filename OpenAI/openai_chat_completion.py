import openai
import os

# Load your API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set up the prompt for the GPT-4 model
prompt = "Create a creative greeting:"

# Call the OpenAI API to generate a response
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

# Print the generated greeting
print(response)