from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    
)
SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Rishi Jha.
    You are acting on behalf of Rishi Jha who is 24 years old tech enthusiast and principle engineer .Your main tech stack is JS and python and you are learning Gen AI this days.

    Examples:
    Q.Hey
    A. Hey,whats up!
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    # response_format={"type": "json_object"},
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT},
        { "role": "user", "content" : "Hey there" }
    ]
)   

print("Response:", response.choices[0].message.content)