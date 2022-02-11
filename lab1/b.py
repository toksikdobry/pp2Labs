s = input()
a = 0
for i in range(len(s)):
    a = a + ord(s[i])
print('It is tasty!') if a > 300 else print('Oh, no!')


