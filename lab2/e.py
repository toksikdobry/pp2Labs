s = input().split()
if len(s) == 1: s.append(input())
n, x, b = int(s[0]), int(s[1]), 0
arr = []
for i in range(n):
    arr.append(x + 2*i)
    b = b ^ arr[i]
print(b)