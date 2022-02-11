s = input()
s = s.split()
arr = []
for i in s:
    sz = len(i)
    if sz >= 3: arr.append(i) 
print(*arr)