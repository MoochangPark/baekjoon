from collections import deque
import copy

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    
    dic = [[] for _ in range(n+1)]
    ind = [0] * (n+1)

    for _ in range(k):
        a, b = map(int, input().split())
        dic[a].append(b)
        ind[b] += 1

    w = int(input())

    ch = [0] * (n+1)

    q = deque()

    for i in range(1, n+1):
        if ind[i] == 0:
            q.append(i)
            ch[i] = cost[i]

    while q:
        now = q.popleft()

        for dn in dic[now]:
            ind[dn] -= 1
            ch[dn] = max(ch[now] + cost[dn], ch[dn])
            if ind[dn] == 0:
                q.append(dn)
    
    print(ch[w])