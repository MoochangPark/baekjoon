n = int(input())
m = int(input())

parent = [0] * (n+1)

for i in range(n):
    parent[i] = i


edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x : x[2])

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

result = 0

for edge in edges:
    a, b, cost = edge
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        result += cost

print(result)