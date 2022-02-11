n = int(input())
arr = []
for i in range(n):
    s = input().split()
    if s[0] == "1": arr.append(s[1])
    elif s[0] == "2": 
        print(arr[0], end = ' ')
        arr.pop(0)
