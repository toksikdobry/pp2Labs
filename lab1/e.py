def isPrime(a):
    k = 0
    for i in range(2, (a // 2) + 1): 
        if a % i == 0: k += 1
    if k <= 0: return True
    else: return False
s = input().split()
dist, count = int(s[0]), int(s[1])
if dist > 500: print('Try next time!')
elif isPrime(dist) == False: print('Try next time!')
elif count % 2 != 0: print('Try next time!')
else: print('Good job!')