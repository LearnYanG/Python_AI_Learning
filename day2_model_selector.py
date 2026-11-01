requested_tokens = 3500
preferred_provider = "Anthropic"
selected_model = None

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

if preferred_provider == models[0]["provider"]:
    selected_model = models[0]
elif preferred_provider == models[1]["provider"]:
    selected_model = models[1]
elif preferred_provider == models[2]["provider"]:
    selected_model = models[2]

if selected_model is None:
    print ("provider not found")
elif requested_tokens > selected_model["max_tokens"]:
    print (f"Select model: {selected_model['name']}")
    print ("Token limit exceeded")
else:
    print (f"Select model: {selected_model['name']}")
    print ("Request allow")
