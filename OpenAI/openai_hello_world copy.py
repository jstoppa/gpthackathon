import openai
import os

# Load your API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set up the prompt for the GPT-4 model
prompt = "Create a creative greeting:"

# Call the OpenAI API to generate a response
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated greeting
print(response.choices[0].text.strip())