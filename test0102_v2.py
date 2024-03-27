import os
import openai
from dotenv import load_dotenv

load_dotenv()
#import keys_info

# need openai version 0.28!!!!

def chatgpt(query):
    # Ensure that the API key is set as an environment variable
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    if OPENAI_API_KEY:
        openai.api_key = OPENAI_API_KEY
    else:
        raise EnvironmentError("OpenAI API key not found in environment variables")

    # Make an API request
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Use the Davinci model
        prompt=query,
        max_tokens=100
    )

    # Extract and print the response
    chatgpt_response = response.choices[0].text
    
    return chatgpt_response
    
if __name__ == '__main__':
    return_answer = chatgpt("Tell me a joke about the celebrity.")
    if return_answer:
        print(return_answer)
    else:
        print("There is no answer")
else:
    print("This is not the main module")


