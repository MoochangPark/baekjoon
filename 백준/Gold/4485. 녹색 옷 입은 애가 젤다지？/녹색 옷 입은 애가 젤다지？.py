import heapq

t = 1
while True:
    n = int(input())
    if n == 0:
        break
    l = [list(map(int, input().split())) for _ in range(n)]
    d = {}
    ch = [[21E8] * n for _ in range(n)]

    q = []

    heapq.heappush(q,(l[0][0],0,0))
    ch[0][0] = 0
    while q:
        cost, y, x = heapq.heappop(q)

        if y == n-1 and x == n-1:
            print(f'Problem {t}: {ch[y][x]}')
        
        for dy, dx in ((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
            if 0 <= dy < n and 0 <= dx < n:
                if cost + l[dy][dx] < ch[dy][dx]:
                    ch[dy][dx] = cost + l[dy][dx]
                    heapq.heappush(q,(ch[dy][dx],dy,dx))
    
    t += 1