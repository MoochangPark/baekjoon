import heapq

n = int(input())
m = int(input())

l = [21E8]*(n+1)
d = {}

for _ in range(m):
    a,b,c = map(int, input().split())
    if a not in d:
        d[a] = []
    d[a].append([b,c])

s,e = map(int, input().split())
l[s] = 0

# r = [[] for _ in range(n+1)]
r = [0] * (n+1)
hq = []
heapq.heappush(hq,[s,0])

while hq:
    now, cost = heapq.heappop(hq)

    if l[now] < cost:
        continue

    if now in d:
        for nextNode, nextCost in d[now]:
            if l[nextNode] > cost+nextCost:
                l[nextNode] = cost+nextCost
                heapq.heappush(hq,[nextNode,cost+nextCost])
                r[nextNode] = now

print(l[e])

path = []
t = e
while t:
    path.append(t)
    t = r[t]
print(len(path))

path = path[::-1]
print(*path)