from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key = "AIzaSyBL1JEYgWn2QBvoy5M1-4ToUx9taQ0JRn0",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
# directly giving instruction to the model is termed as zero short prompting
SYSTEM_PROMPT = """
You should only and only answer the coding related questions.Do not answer anything else your name is alexa if user asked something other then coding just say sorry

Examples:
Q.can you explain the a+b whole square?
A.Sorry,I can only help with the codding related questions

        Q. Hey ,Write a code in python for adding two numbers.
        A. def add(a,b):
        return a + b
"""
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        { "role": "user", "content" : "can you explain me a + b whole square" }
    ]
)

print(response.choices[0].message.content)
# the model is given direct question  or task without prior examples


# few_shot_promoting = The model is provided with the few examples before asking it to generate  a response.