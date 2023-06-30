import heapq

v, e = map(int, input().split())

k = int(input())

l = {}

answer = [21e8] * (v+1)

answer[k] = 0

for i in range(e):
    a, b, c = (list(map(int, input().split())))
    if a in l:
        l[a].append([b,c])
    else:
        l[a] = []
        l[a].append([b,c])

hq = []
heapq.heappush(hq, (0,k))

while hq:
    cost, now = heapq.heappop(hq)

    if now in l:
        for nextNode, nextCost in l[now]:
            if cost + nextCost < answer[nextNode]:
                answer[nextNode] = cost + nextCost
                heapq.heappush(hq, (cost+nextCost, nextNode))

for i in range(len(answer)):
    if i == 0:
        continue
    elif answer[i] == 21E8:
        print('INF')
    else:
        print(answer[i])