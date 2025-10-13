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

Output Format:
{{
"code": "string" or null,
"isCodingQuestion": boolean
}}
Examples:
Q.can you explain the a+b whole square?
A.{{ "code": null, "isCodingQuestion": false}}

        Q. Hey ,Write a code in python for adding two numbers.
        A. {{ "code": "def add(a,b):
        return a + b", "isCodingQuestion": false}}
"""
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        { "role": "user", "content" : "Hey,write a code to add n numbers in javascript" }
    ]
)

print(response.choices[0].message.content)
# the model is given direct question  or task without prior examples


# few_shot_promoting = The model is provided with the few examples before asking it to generate  a response.