from collections import deque

def bfs(y, x):
    q = deque()
    q.append([y,x])
    check[y][x] = 1
    seaList = []

    while q:
        qy, qx = q.popleft()
        sea = 0
        for dy, dx in ((-1,0), (1,0), (0,-1), (0,1)):
            ny = qy + dy
            nx = qx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if not l[ny][nx]:
                    sea += 1
                elif l[ny][nx] and not check[ny][nx]:
                    q.append([ny, nx])
                    check[ny][nx] = 1
        if sea > 0:
            seaList.append((qy, qx, sea))
    
    for yy, xx, sea in seaList:
        l[yy][xx] = max(0, l[yy][xx] - sea)

    return 1


n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if l[i][j]:
            ice.append((i, j))

answer = 0

while ice:
    check = [[0] * m for _ in range(n)]
    delice = []
    group = 0
    for i, j in ice:
        if l[i][j] and not check[i][j]:
            group += bfs(i, j)
        if l[i][j] == 0:
            delice.append((i, j))
    if group > 1:
        print(answer)
        break
    ice = sorted(list(set(ice) - set(delice)))
    answer += 1

if group < 2:
    print(0)