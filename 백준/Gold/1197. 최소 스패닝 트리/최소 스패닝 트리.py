v, e = map(int, input().split())

edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))
edges.sort(key=lambda x : x[2])

l = [i for i in range(v+1)]

def get_parent(x):
    if l[x] == x:
        return x
    l[x] = get_parent(l[x])
    return l[x]

def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        l[b] = a
    else:
        l[a] = b

def same_parent(a,b):
    return get_parent(a) == get_parent(b)

answer = 0

for a, b, cost in edges:
    if not same_parent(a,b):
        union_parent(a,b)
        answer += cost
print(answer)
