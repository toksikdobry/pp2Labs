import re
s = input()
t = r'[A-Z][a-z]'
x = re.findall(t, s)
if x: print("True") 
else: print("False")