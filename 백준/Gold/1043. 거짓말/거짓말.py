n, m = map(int, input().split())

know = list(map(int, input().split()))[1:]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#초기화
parent = [i for i in range(n+1)]
for k in know:
    parent[k] = 0


parties = []

for _ in range(m):
    p = list(map(int, input().split()))
    pn = p[0]
    pl = p[1:]

    for i in range(pn-1):
        union(pl[i], pl[i+1])
    parties.append(pl)

answer = 0

for party in parties:
    k = False
    for i in range(len(party)):
        if find(party[i]) == 0:
            k = True
            break
    if not k:
        answer += 1

print(answer)
