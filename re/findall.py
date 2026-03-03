import re

text = "I have 2 cats and 3 dogs"
matches = re.findall(r"\d", text)

print(matches)