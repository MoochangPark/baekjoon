import heapq

n, k = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

bag = []
for _ in range(k):
    bag.append(int(input()))

l.sort()
bag.sort()

answer = 0
hq = []

for b in bag:
    while l and l[0][0] <= b:
        heapq.heappush(hq, -l[0][1])
        heapq.heappop(l)
    if hq:
        answer -= heapq.heappop(hq)
print(answer)