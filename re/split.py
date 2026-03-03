import re

text = "apple,banana;cherry"
result = re.split(r"[;,]", text)

print(result)