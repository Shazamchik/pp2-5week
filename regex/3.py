import re
txt = "aa_b ddd_aa eeeff"
x = re.findall("[a-z]+_[a-z]+", txt)
print(x)