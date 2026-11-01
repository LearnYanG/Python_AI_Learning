name = "yan"
age = 24
height = 1.80
is_student = True
model_name = "GPT_6"
tokens = 1000
price_per_token = 0.002

total_cost = tokens * price_per_token

print(name)
print(age)
print(height)
print(is_student)
print(total_cost)


print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

print(type(model_name))
print(type(total_cost))


role = "Python teacher"
task = "Explain variables"
level = "Beginner"


print(f"you are a {role}, Please {task} for a {level}.")