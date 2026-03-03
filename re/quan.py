import re

print(re.findall(r"\d+", "123 45"))   # + (one or more)
print(re.findall(r"ab*", "a ab abb"))  # * (zero or more)
print(re.findall(r"colou?r", "color colour"))  # ? (optional)
print(re.findall(r"\d{2}", "1234"))  # exactly 2 digits