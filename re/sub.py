import re

text = "My number is 12345"
result = re.sub(r"\d", "*", text)

print(result)