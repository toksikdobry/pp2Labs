a = int(input())
typ = input()
if typ == 'k':
    c = int(input())
    cz = "{:." + str(c) + "f}"
    a = cz.format(a / 1024)
elif typ == 'b':
    a = a * 1024
print(a)