from collections import deque

n, m = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    q = deque()
    q.append([0,0])
    v[0][0] = 1

    while q:
        y, x = q.popleft()

        for dy, dx in ((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
            if 0 <= dy < n and 0 <= dx < m:
                if l[dy][dx] == 0 and v[dy][dx] == 0:
                    q.append([dy,dx])
                    v[dy][dx] = 1
                elif l[dy][dx] == 1:
                    v[dy][dx] += 1
t = 0
while True:
    v = [[0] * m for _ in range(n)]

    bfs()
    
    t += 1
    finish = True
    for i in range(n):
        for j in range(m):
            if l[i][j] == 1:
                if v[i][j] >= 2:
                    l[i][j] = 0
                else:
                    finish = False
    
    if finish:
        print(t)
        break
