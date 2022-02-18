arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primes = list(filter(lambda a: all(a%n!=0 for n in range(2, a//2+1)), arr))
print(*primes)