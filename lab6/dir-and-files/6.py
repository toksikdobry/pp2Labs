import os
path = input()
try:
    os.chdir(path)
    for i in range(65, 91):
        file = open(chr(i)+'.txt', 'w')
except Exception as e:
    print(e)
