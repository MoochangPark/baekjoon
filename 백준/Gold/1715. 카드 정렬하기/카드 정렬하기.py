import heapq

n = int(input())

hq = []

for i in range(n):
    heapq.heappush(hq,int(input()))

if len(hq) == 1:
    print(0)
else:
    answer = 0
    while len(hq) > 1:
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        answer += a + b
        heapq.heappush(hq,a+b)

    print(answer)