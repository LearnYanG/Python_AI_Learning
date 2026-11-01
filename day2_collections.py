models = ["GPT-6", "claude", "Gemini"]
models.append("Llama")
print(models[0], models[3])

ai_model = {
    "name" : "GPT-6",
    "provider" : "OpenAI",
    "max_token" : 1000
}

ai_model["max_token"] = 2000

print(ai_model["name"], ai_model["max_token"])