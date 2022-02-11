n = int(input())
dem, hunt = {}, {}
for i in range (n):
    d, w = input().split()
    if dem.get(w) == None: dem[w] = 1
    else: dem[w] += 1
m = int(input())
for i in range(m):
    h, a, k = input().split()
    s = int(k)
    if dem.get(a) == None: hunt[a] = s
    else: dem[a] -= s
survivors = 0
for j in dem.values():
    if j > 0: survivors += j
print (' Demons left:', survivors)