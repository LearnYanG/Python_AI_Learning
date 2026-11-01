user_input = input("Enter token amount: ")

try:
    tokens = int(user_input)
    if tokens < 0:
        print("Tokens cannot be negative")
    else:
        print(f"Valid tokens: {tokens}")
except ValueError:
    print("Invalid input")