models = [
    {
        "name":"GPT-6",
        "provider":"OpenAI",
        "max_tokens":4000
    },
    {
        "name": "Claude",
        "provider": "Anthropic",
        "max_tokens": 3000
    },
    {
        "name": "Gemini",
        "provider": "Google",
        "max_tokens": 2000
    }
]

def select_model(provider, models): 
    for model in models:
        if model["provider"] == provider:
            return model
    return None

result = select_model("Anthropic", models)
print(result["name"])