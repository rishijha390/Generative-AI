from google import genai

client = genai.Client(
    api_key="AIzaSyBL1JEYgWn2QBvoy5M1-4ToUx9taQ0JRn0"
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
) 

print(response.text)