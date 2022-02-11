n = int(input())
arr = []
for i in range(n):
    s = input()
    if "gmail.com" in s: arr.append(s[:-10])
for i in arr: print(i)



