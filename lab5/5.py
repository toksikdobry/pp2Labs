import re
s = input()
t = r'a(\w)*b$'
x = re.findall(t, s)
if x: print("True")
else: print("False")