import re
s = input()
t = r'^ab{2,3}$'
x = re.findall(t, s)
if x: print("True")
else: print("False")