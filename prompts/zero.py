from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key = "#",
    base_url="#"
)
# directly giving instruction to the model is termed as zero short prompting
SYSTEM_PROMPT = "You should only and only answer the coding related questions.Do not answer anything else your name is alexa if user asked something other then coding just say sorry"
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        { "role": "user", "content" : "can you tell me a joke" }
    ]
)

print(response.choices[0].message.content)
# the model is given direct question  or task without prior examples
