import random

#1 task
def gramsToOunces(grams):
    ounces = grams / 28.3495231
    print(ounces)

#2 task
def fahrenheitToCelsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    print(celsius)

#3 task   
def solve(numheads, numlegs):
    rabbits = 0.5 * numlegs - numheads
    chickens = 2 * numheads - 0.5 * numlegs
    print("Rabbits =", rabbits)
    print("Chickens =", chickens)

#4 task
def filter_prime():
    s = list(map(int, input().split()))
    for number in s:
        if number < 2: s.remove(number)
        elif number == 2: continue
        else:
            for i in range(2, number):
                if number % i == 0:
                    s.remove(number)
                    
    return print(*s)            

#5 task
def allPermut():
    s = input().split()
    for i in range(len(s)):
        for j in range(len(s)-1):
            print(*s)
            s[j], s[j+1] = s[j+1], s[j]

#6 task
def reversed():
    s = input().split()
    print(*s[::-1])

#7 task
def has_33(nums):
    for i in range(len(nums)):
        if nums[i] == 3 and nums[i-1] == 3:     #nums = [1, 2, 3, 3]
            return True                         #nums = [1, 3, 2, 3]
    else:                                       #nums = [1, 0, 0]
        return False                        

#8 task
def spy_game(nums):
    for i in nums: 
        if i == 7: 
          num = nums[:nums.index(i)]    #nums = [1, 0, 2, 7, 0, 1]           
    if len(num) == len(nums):           #nums = [0, 0, 0, 7, 0, 1]           
        return False                    #nums = [0, 0, 2, 7, 0, 1]           
    cnt = 0
    for j in num:
        if j == 0: cnt += 1
    if cnt >= 2: 
        return True
    else: 
        return False

#9 task
def spherevol(r):
    volume = 4/3 * 3.14159 * r ** 3
    print(volume)

#10 task
def unique(list):
    arr = []
    for i in list:
        if i not in arr: arr.append(i)      #s =[1, 2, 3, 1, 1, 2, 0, 5]
    print(arr)

#11 task
def palindrome():
    word = input()
    for i in range(len(word)):
        if word[i] != word[-(i+1)]:
            return print("The word is not a palindrome")
    return print("The word is a palindrome")

#12 task
def histogram(s):
    for i in s:
        for j in range(i): print("*", end="")       #s = [1, 3, 5, 7, 2, 6]
        print()    

#13 task
def guessthenumber():
    print("Hello! What is your name?")
    name = input()
    print("Well, ", name, ", I am thinking of a number between 1 and 20.", sep = "")
    print("Take a guess.")
    cnt = 0
    r = random.randint(1, 20)
    while 1:
        n = int(input())
        if n > r: 
            print("Your guess is too large")
            cnt += 1
            print("Take a guess.")
        elif n < r:
            print("Your guess is too low")
            cnt += 1
            print("Take a guess.")
        else:
            cnt += 1
            print("Good job, ", name, "! You guessed my number in ", cnt, " guesses!", sep = "")
            break


# gramsToOunces(5)
# fahrenheitToCelsius(5)
# solve(35,94)
# filter_prime()
# allPermut()
# reversed()
# has_33(nums)
# spy_game(nums)
# spherevol(2)
# unique(s)
# palindrome()
# histogram([1, 3, 5, 7, 2, 6])
# guessthenumber()








    
    