from collections import defaultdict
def yanelyublyupython():
    return 0

students, bucks = defaultdict(yanelyublyupython), 0
for i in range(int(input())):
    name, money = input().split() 
    students[name] += int(money) 
    if students[name] > bucks: 
        bucks = students[name]

sortStudents = sorted(students)

for i in sortStudents:
    if students[i] == bucks:
        print(i, 'is lucky!')
    else:
        out = bucks - students[i]
        print(i, 'has to receive', out, 'tenge')