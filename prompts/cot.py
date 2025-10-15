import os
import json
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

# client = OpenAI(
#       api_key = "AIzaSyBL1JEYgWn2QBvoy5M1-4ToUx9taQ0JRn0",
#       base_url="https://generativelanguage.googleapis.com/v1beta/"
# )
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thoughts.
    You work on START, PLAN AND OUTPUT steps.
    You need to first PLAN  what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input),PLAN(that can be multiple times) and finally OUTPUT (which is going to be displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string"}

    Example:
    START: Hey,Can you solve 2 + 3 * 5 /10
    PLAN: {"step": "PLAN": "content": "looking at the problem, we should solve this
    using BODMAS method"}
    PLAN: {"step": "PLAN": "content": "Yes,The BODMAS is correct thing to be doe here" }
    PLAN: { "step": "PLAN": "content":"first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content":"now we must divide 15 / 10 which is 1.5" }
    PLAN: { "step": "PLAN": "content":"now we must add 1.5 + 2 which is 3.5" }
    OUTPUT: {"step": "OUTPUT": "content": "The answer is 3.5"}

 """

message_history = [
    { "role": "system" , "content": SYSTEM_PROMPT },
]

user_query = input("👉 ")
message_history.append({ "role": "user" , "content": user_query })

while True:
    response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=message_history    
    )

    raw_result = (response.choices[0].message.content)
    message_history.append({"role": "assistant" , "content": raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("💡", parsed_result.get("content"))
        break
     
# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     response_format={"type": "json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         { "role": "user", "content" : "Hey,write a code to add n numbers in javascript" },
#         { "role": "assistant", "content": json.dumps({"step": "START", "content": "You want a JavaScript code to add 'n' numbers." })},
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "To add 'n' numbers in JavaScript, I will define a function that accepts an arbitrary number of arguments using the rest parameter syntax. Inside the function, I will use the `reduce` array method to sum all the provided numbers. I will then provide the JavaScript code snippet." })}
#     ]
# )

# print(response.choices[0].message.content)