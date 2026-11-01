import json
ai_model = {
    "name" : "GPT-6",
    "provider" : "OpenAI",
    "max_tokens" : 4000,
    "available" : True
}

json_text = json.dumps(ai_model)

print(json_text)
print(type(json_text))

python_data = json.loads(json_text)

print(python_data["name"])
print(python_data["available"])