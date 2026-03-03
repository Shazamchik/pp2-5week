import re
txt = "abbb abb ab"
x = re.findall("ab{2,3}", txt)
print(x)