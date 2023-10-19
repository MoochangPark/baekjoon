from collections import deque

n, m = map(int, input().split())

c = [0] * (n+1)

g = [[] for _ in range(n+1)]

for _ in range(m):
    l = list(map(int, input().split()))
    for i in range(1,l[0]):
        g[l[i]].append(l[i+1])
        c[l[i+1]] += 1

def bfs():
    result = []
    q = deque()

    for i in range(1, n+1):
        if c[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        
        for i in g[now]:
            c[i] -= 1
            
            if c[i] == 0:
                q.append(i)
    
    if len(result) != n:
        print(0)
    else:
        for r in result:
            print(r)

bfs()