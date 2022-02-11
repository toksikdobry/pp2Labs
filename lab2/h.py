singlePoint = list(map(int, input().split()))
n = int(input())
arrPoints = []
for i in range(n): 
    point = list(map(int, input().split()))
    r = ((point[0] - singlePoint[0])**2 + (point[1] - singlePoint[1])**2)**(0.5)
    arrPoints.append((r, point))
arrPoints.sort(key = lambda x: x[0])
for j in arrPoints: print(*j[1])
        