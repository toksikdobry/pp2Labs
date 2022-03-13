import re
s = input()
t = r"(\w)([A-Z])"
t2 = r"\1 \2"
x = re.sub(t, t2, s)
print(x)