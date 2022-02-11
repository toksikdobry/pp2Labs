def word(a):
    up, low, dig = False, False, False
    for symbol in a:
        if symbol >= 'A' and symbol <= 'Z': up  = True
        if symbol >= '0' and symbol <= '9': dig = True
        if symbol >= 'a' and symbol <= 'z': low = True
    if up and low and dig: 
        return True
    else:                  
        return False
        
n = int(input())
arr = []
for i in range(n):
    s = input()
    if word(s) and s not in arr: arr.append(s)
arr.sort()
print(len(arr))
for k in arr: print(k)
