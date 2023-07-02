import heapq

n,m,x = map(int, input().split())

d = {}

for i in range(m):
    a, b, c = map(int, input().split())

    if a not in d:
        d[a] = []
    d[a].append([b,c])

def dijk(start):
    global n

    l = [21E8] * (n+1)
    l[start] = 0
    
    hq = []
    heapq.heappush(hq, (0,start))

    while hq:
        cost, now = heapq.heappop(hq)

        if now in d:
            for nextDir, nextCost in d[now]:
                if cost + nextCost < l[nextDir]:
                    l[nextDir] = cost + nextCost
                    heapq.heappush(hq, (cost + nextCost, nextDir))
    return l

maxs = 0

xx = dijk(x)
for i in range(1, n+1):
    ll = dijk(i)
    maxs = max(maxs, ll[x] + xx[i])
print(maxs)