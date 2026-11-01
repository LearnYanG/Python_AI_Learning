import json

messages = [
    {
        "role" : "user",
        "content" : "What is Python?"
    },
    {
        "role": "assistant",
        "content": "Python is a programming language."
    },
]

with open ("chat_history.json", "w", encoding= "UTF-8") as file:
    json.dump(messages, file, indent = 4)
with open ("chat_history.json", "r", encoding= "UTF-8") as file:
    get_messages = json.load(file)

print (get_messages[0]["content"])
print (get_messages[1]["role"])
