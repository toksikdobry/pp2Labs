import re
s = input()
t = r'(\w)_+(\w)'
x = re.findall(t, s)
if x: print("True")
else: print("False")