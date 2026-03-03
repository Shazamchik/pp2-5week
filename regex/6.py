import re
txt = "Hello, Jon. How are you?"
x = re.sub("[\s.,]", ":", txt)
print(x)