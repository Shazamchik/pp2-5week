import re

text = "I have 2 cats and 3 dogs"
match = re.search(r"\d", text)

print(match)