import heapq

n, m = map(int, input().split())
answer = []

l = [[] for _ in range(n+1)]
ins = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    l[a].append(b)
    ins[b] += 1

hq = []

for i in range(1, n+1):
    if ins[i] == 0:
        heapq.heappush(hq, i)

while hq:
    q = heapq.heappop(hq)
    answer.append(q)
    for i in l[q]:
        ins[i] -= 1
        if ins[i] == 0:
            heapq.heappush(hq, i)

print(*answer)