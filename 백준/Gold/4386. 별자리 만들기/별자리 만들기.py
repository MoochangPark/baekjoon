from math import sqrt

v = int(input())

parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

l = []
edges = []
result = 0

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

for _ in range(v):
    y, x = map(float, input().split())
    l.append([y,x])

for i in range(v-1):
    for j in range(i+1, v):
        c = sqrt((l[i][0] - l[j][0])**2 + (l[i][1] - l[j][1])**2)
        edges.append([c,i,j])

edges.sort()

for edge in edges:
    c, y, x = edge
    if find(y) != find(x):
        union(y,x)
        result += c

print(round(result,2))