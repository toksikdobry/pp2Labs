import re
s = input()
t = r'[A-Za-z][^A-Z]*'
x = re.findall(t, s)
print(*x)