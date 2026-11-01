import json

try:
    with open("chat_history.json", "r", encoding="utf-8") as file:
        messages = json.load(file)
except FileNotFoundError:
    messages = []

user_message = input("You: ")

ai_response = "I received your message."

messages.append(
    {
        "role" : "user",
        "content" : user_message
    })
    
messages.append( 
    {
        "role" : "assistant",
        "content" : ai_response
    })

with open ("chat_history.json", "w", encoding= "UTF-8") as file:
    json.dump(messages, file, indent= 4)

print(f"AI: {ai_response}")
print(len(messages))

