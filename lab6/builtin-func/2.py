string = input()
up, low = 0, 0
for i in string:
    if ord(i) >= 65 and ord(i) <= 90:
        up += 1
    elif ord(i) > 97 and ord(i) <= 122:
        low += 1
print("Upper case:", up)
print("Lower case:", low)