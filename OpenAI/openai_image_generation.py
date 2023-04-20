import openai
import os

# Load your API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set up the prompt for the GPT-4 model
prompt = "a white siamese cat"

# Call the OpenAI API to generate a response
response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

# Print the generated greeting
print(image_url)