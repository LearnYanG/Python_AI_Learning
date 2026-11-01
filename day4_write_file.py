user_message = "What is Python?"
ai_response = "Python is a programming language."

with open ("chat_log.txt", "w", encoding="UTF-8") as file:
    file.write(f"User: {user_message}\n")

with open ("chat_log.txt", "a", encoding="UTF-8") as file:
    file.write(f"AI: {ai_response}")

print("successful")
