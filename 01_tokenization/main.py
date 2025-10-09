import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Rishi Jha"
tokens = enc.encode(text)

# Tokens [25216, 3274, 0, 3673, 1308, 382, 460, 24597, 643, 1716]
print("Tokens" , tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 460, 24597, 643, 1716])
print("Decoded ", decoded)
# Decoded  Hey There! My name is Rishi Jha