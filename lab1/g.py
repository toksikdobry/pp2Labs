def toDec(a):
    if a == 1 or a == 0: return a
    size = len(str(a)) - 1
    b = a // pow(10, size)
    return (pow(2, size) * b) + toDec(a % pow(10, size))
bin = int(input())
print(toDec(bin))
