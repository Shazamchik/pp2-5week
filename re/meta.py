import re

print(re.findall(r"c.t", "cat cot cut"))   # .  (any character)
print(re.findall(r"^Hello", "Hello World"))  # ^ (start)
print(re.findall(r"World$", "Hello World"))  # $ (end)
print(re.findall(r"[ae]", "apple"))  # [] 
print(re.findall(r"cat|dog", "cat dog"))  # | (OR)
print(re.findall(r"He.{2}o", "Hello World")) # Exactly the specified number of occurrences
