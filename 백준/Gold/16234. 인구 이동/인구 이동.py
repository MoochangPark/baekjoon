from collections import deque

n, L, R = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(n)]

count = []

def bfs(y,x,v):
    group = []
    q = deque()

    q.append([y,x])
    group.append([y,x])

    while q:
        qy, qx = q.popleft()

        for dy, dx in [(qy+1,qx),(qy-1,qx),(qy,qx+1),(qy,qx-1)]:
            if 0 <= dy < n and 0 <= dx < n:
                if v[dy][dx] == 0:
                    if L <= abs(l[dy][dx] - l[qy][qx]) <=R:
                        v[dy][dx] = 1
                        q.append([dy,dx])
                        group.append([dy,dx])
    return group

answer = 0

while True:
    flag = 0
    v = [[0] * (n+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                v[i][j] = 1
                count = bfs(i,j,v)
                if len(count) > 1:
                    flag = 1
                    same = sum([l[y][x] for y,x in count]) // len(count)
                    for y, x in count:
                        l[y][x] = same
    if flag == 0:
        break
    answer += 1

print(answer)