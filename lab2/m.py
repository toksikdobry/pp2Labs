arr = []
while True:
    date = input()
    if date == "0": 
        break
    day, month, year = date.split()
    dates = (year, month, day)
    arr.append(dates)
sortArr = sorted(arr)
for i in sortArr:
    print(*i[::-1])