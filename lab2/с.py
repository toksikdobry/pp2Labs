n = int(input())
for i in range(n):
    for j in range(n):
        if j == 0: print(i, end = " ")
        elif i == 0: print(j, end = " ")
        elif i == j: print(i * j, end = " ")
        elif i != 0 and j != 0: print(0, end = " ")
    print()