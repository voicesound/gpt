
import openai
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Debugging line to check if the .env file is being read
print("Environment variables:", os.environ)

# Debugging line to check if the API key is loaded
api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key: {api_key}")

if api_key is None:
    raise ValueError("API key not found. Ensure the .env file is correctly formatted and in the right directory.")

# Set the API key
openai.api_key = api_key

def get_completion(prompt, model= "gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    try:
        response = openai.chat.completions.create(
           model=model,
            messages=messages,
            max_tokens=50,
            temperature=0,
        )
        return response.choices[0].message.content
    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return "An error occurred. Please try again later."
    
    
   

prompt = "How far away is the moon?"
print(get_completion(prompt))

