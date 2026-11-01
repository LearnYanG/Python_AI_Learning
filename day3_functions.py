def greet_user(name):
    print(f"Hello, {name} Welcome to AI Learing")
greet_user("Yan")

def calculate_cost(tokens, price):
    cost = tokens * price
    return cost
result = calculate_cost(2000, 0.003)
print (result)


def check_tokens(tokens, max_tokens):
    if tokens > max_tokens:
        return "Token limit exceeded"
    return "Request allowed"

result = check_tokens(1500, 2000)
result1 = check_tokens(2500, 2000)
result2 = check_tokens(2000, 2000)

print(result, result1, result2)