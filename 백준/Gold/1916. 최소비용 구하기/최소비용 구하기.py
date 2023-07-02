import heapq

n = int(input())
m = int(input())

hq = []

d = {}

for i in range(m):
    a, b, c = map(int, input().split())

    if a not in d:
        d[a] = []
    d[a].append([b,c])


start, end = map(int, input().split())

heapq.heappush(hq, [0,start])

answer = [21E8] * (n+1)
answer[0] = 0

while hq:
    cost, now = heapq.heappop(hq)

    if now == end:
        break

    if now in d:
        for nextDir, nextCost in d[now]:
            if cost + nextCost < answer[nextDir]:
                answer[nextDir] = cost + nextCost
                heapq.heappush(hq,(cost + nextCost, nextDir))
                
print(answer[end])