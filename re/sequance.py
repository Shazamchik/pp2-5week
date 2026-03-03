import re

print(re.findall(r"\d", "A1B2"))   # digit
print(re.findall(r"\w", "Hi_5"))   # word character
print(re.findall(r"\s", "Hi There"))  # space
print(re.findall(r"\D", "Hi_7")) #DOES NOT contain digits
print(re.findall(r"\W", "Hi.7")) #DOES NOT contain any word characters