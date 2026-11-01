import json

ai_model = {
    "name": "GPT-6",
    "provider": "OpenAI",
    "max_tokens": 4000,
    "available": True
}

with open("model.json", "w", encoding="utf-8") as file:
    dumped_model = json.dump(ai_model, file, indent=4)

print("JSON file saved!")
print(dumped_model)
print(type(dumped_model))

with open("model.json", "r", encoding="utf-8") as file:
    loaded_model = json.load(file)

print(loaded_model)
print(type(loaded_model))