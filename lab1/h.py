word = input()
letter = input()
a = []
n = -1
for x in word:
    n += 1
    if letter == x:
        a.append(n)
print(a[0]) if a[0] == a[-1] else print( a[0], a[-1] )
