from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

# Configure OpenAI with your API key
openai.api_key = os.getenv('OPENAI_API_KEY')

try:
    # Test the API connection
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "Hello, are you working?"}
        ]
    )
    print("API Connection Successful!")
    print("Response:", response.choices[0].message.content)
    
except Exception as e:
    print("Error:", str(e)) 