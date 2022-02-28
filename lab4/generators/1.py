def squares(a, b):
    while a < b:
        a += 1
        yield a*a
for i in squares(0, 10):
    print(i, end = " ")