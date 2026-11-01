tokens = 1500
max_tokens = 2000
api_key_valid = True

if api_key_valid != True:
    print("Invalid API Key")
elif api_key_valid == True and tokens > max_tokens:
    print("Token limit exceeded")
elif api_key_valid == True and tokens <= max_tokens:
    print("Request allowed")