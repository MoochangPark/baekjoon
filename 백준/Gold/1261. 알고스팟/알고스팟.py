import heapq

m, n = map(int, input().split())

l = [list(map(int, input())) for _ in range(n)]

hq = []

ch = [[21E8] * m for _ in range(n)]

heapq.heappush(hq,[0,0,0])
ch[0][0] = 0
while hq:
    cost, y, x = heapq.heappop(hq)

    for dy, dx in ((y-1,x),(y+1,x),(y,x-1),(y,x+1)):
        if 0 <= dy < n and 0 <= dx < m:
            if cost + l[dy][dx] < ch[dy][dx]:
                ch[dy][dx] = cost + l[dy][dx]
                heapq.heappush(hq,[cost+l[dy][dx], dy, dx])
print(ch[n-1][m-1])
