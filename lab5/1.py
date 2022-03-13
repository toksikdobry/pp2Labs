import re
s = input()
t = r'^a(b*)$'
x = re.findall(t, s)
if x: print("True")
else: print("False")
