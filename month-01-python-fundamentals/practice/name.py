def greet_user(name, age):
    name = str(name).capitalize()
    age = int(age)
    if age >= 18:
        return f"Hello, {name}! You are an adult, {age} years old."
    else:
        return f"Hello, {name}! You are a minor, {age} years old."


result = greet_user("Alice" , 20)
print(result)