from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key = "AIzaSyBL1JEYgWn2QBvoy5M1-4ToUx9taQ0JRn0",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = "You should only and only answer the coding related questions.Do not answer anything else your name is alexa if user asked something other then coding just say sorry"
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        { "role": "user", "content" : "Solve a + b whole square" }
    ]
)

print(response.choices[0].message.content)
