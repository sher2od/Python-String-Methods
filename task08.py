text = input()
start = input()
result = text.islower() and text.startswith(start.lower())
print(result)