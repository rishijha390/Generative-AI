from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key = "AIzaSyBL1JEYgWn2QBvoy5M1-4ToUx9taQ0JRn0",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "user", "content" : "Hey There, I am Rishi Jha, a software developer. Can you tell me a joke?" }
    ]
)

print(response.choices[0].message.content)