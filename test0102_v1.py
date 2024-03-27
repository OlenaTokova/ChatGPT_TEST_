import os
import openai
import keys_info

# need openai version 0.28!!!!

#os.environ['OPENAI_API_KEY']="OPENAI_API_KEY"

# Ensure that the API key is set as an environment variable
if 'OPENAI_API_KEY' in os.environ:
    openai.api_key = os.environ['OPENAI_API_KEY']
else:
    raise EnvironmentError("OpenAI API key not found in environment variables")

query = "Tell me a joke about the weather."

# Make an API request
response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",  # Use the Davinci model
    prompt=query,
    max_tokens=100
)

# Extract and print the response
chatgpt_response = response.choices[0].text
print("ChatGPT Response:", chatgpt_response)