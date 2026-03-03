import re
txt = "Hello, Abbracham"
x = re.findall(r"ab*", txt, flags = re.IGNORECASE)
print(x)