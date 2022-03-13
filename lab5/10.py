import re
c = input()
s = re.sub(r'(\w)([A-Z])',r'\1_\2',c).lower()
print(s)