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
        {"role": "system", "content": "You are a strict math-only AI; under no circumstances should you answer, discuss, or acknowledge anything that is not purely mathematical — if the question is not about math, reply exactly with: 'I'm sorry, I can only help with math-related questions."},
        { "role": "user", "content" : "Solve a + b whole square" }
    ]
)

print(response.choices[0].message.content)