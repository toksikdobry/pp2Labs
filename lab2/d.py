n = int(input())
k = n
if n % 2 == 0:
    for i in range(n):
        for j in range(n-k+1): print("#", end = "")
        for i in range(k-1): print(".", end = "")
        k -= 1
        print()
else:
    for i in range(n):
        for j in range(k-1): print(".", end = "")
        for i in range(n-k+1): print("#", end = "")
        k -= 1
        print()