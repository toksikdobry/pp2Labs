s = input()
iDontLikePython = 0
while "[]" in s or "()" in s or "{}" in s:
    if "()" in s: s = s.replace("()", "")
    if "[]" in s: s = s.replace("[]", "")
    if "{}" in s: s = s.replace("{}", "")
    iDontLikePython += 1
if len(s) > 0: print("No")
else: print("Yes")