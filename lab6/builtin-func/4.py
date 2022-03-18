import time
num = float(input())
ms = int(input())
time.sleep(ms/1000)
print(f"Square root of {num} after {ms} mileseconds is {num**0.5}")