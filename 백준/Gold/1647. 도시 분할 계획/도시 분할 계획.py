n, m = map(int, input().split())

parent = [0] * (n+1)

edges = []
answer = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

def find(e):
    if parent[e] != e:
        parent[e] = find(parent[e])
    return parent[e]

def union(a, b):
    A = find(a)
    B = find(b)
    
    if A < B:
        parent[B] = A
    else:
        parent[A] = B

last = 0
for edge in edges:
    c, a, b = edge

    if find(a) != find(b):
        union(a,b)
        answer += c
        last = c
    
print(answer - last)