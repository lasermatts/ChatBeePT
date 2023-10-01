# Handles all interactions with the ChatGPT API, including sending requests and handling responses.

import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is loaded
if api_key is None:
    raise ValueError("API Key for OpenAI is missing")

# API endpoint
api_url = "https://api.openai.com/v1/engines/davinci-codex/completions"

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

def query_chatgpt(prompt, max_tokens=50, temperature=0.7):
    """
    Send a prompt to ChatGPT and return the model's response.
    
    :param prompt: str, input prompt for ChatGPT
    :param max_tokens: int, maximum length of the response
    :param temperature: float, sampling temperature for randomness in response
    :return: str, ChatGPT response
    """
    # Payload
    payload = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    # Make API request
    response = requests.post(api_url, json=payload, headers=headers)
    
    # Handle possible errors
    if response.status_code != 200:
        raise ConnectionError(f"Failed to retrieve response from API: {response.status_code}")

    # Extract and return the model's response
    response_content = response.json()
    chatgpt_response = response_content['choices'][0]['text'].strip()
    return chatgpt_response
