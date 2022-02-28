def squares(b):
    cnt = 0
    while cnt < b**0.5:
        cnt += 1
        yield cnt*cnt
a = int(input())
b = int(input())
for i in range(a, b):
    if i in squares(b):
        print(i, end = " ")