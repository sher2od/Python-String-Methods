email = input()

result = not email.startswith("@") and email.endswith(".com")

print(result)