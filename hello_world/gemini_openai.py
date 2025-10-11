from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key = "##",
    base_url="##"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "user", "content" : "Hey There, I am Rishi Jha, a software developer. Can you tell me a joke?" }
    ]
)

print(response.choices[0].message.content)
