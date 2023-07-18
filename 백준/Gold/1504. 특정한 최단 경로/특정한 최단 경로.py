import heapq

n, e = map(int, input().split())

d = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())

    d[a].append([b,c])
    d[b].append([a,c])

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    global n
    answer = [21E8] * (n+1)
    answer[start] = 0
    
    hq = []
    heapq.heappush(hq, [0,start])

    while hq:
        cost, now= heapq.heappop(hq)
        
        if cost > answer[now]:
            continue

        for NextNode, NextCost in d[now]:
            c = answer[now] + NextCost
            if c < answer[NextNode]:
                answer[NextNode] = c
                heapq.heappush(hq, [answer[NextNode], NextNode])

    return answer[end]

r1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n)
r2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n)

if r1 >= 21E8 and r2 >= 21E8:
    print(-1)
else:
    print(min(r1,r2))