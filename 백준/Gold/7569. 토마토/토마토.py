from collections import deque

m,n,h = map(int, input().split())

tomato = m * n * h

l = [[[0] * m for _ in range(n)] for _ in range(h)]


q = deque()

for i in range(h):
    for j in range(n):
        t = list(map(int, input().split()))
        for k in range(m):
            l[i][j][k] = t[k]
            if l[i][j][k] == 1 or l[i][j][k] == -1:
                tomato -= 1
                if l[i][j][k] == 1:
                    q.append([i,j,k,0])

def bfs():
    global tomato
    answer = 0
    while q:
        qz, qy, qx, qday = q.popleft()

        for x, y, z, in ((-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)):
            qxx = qx + x
            qyy = qy + y
            qzz = qz + z

            if 0 <= qxx < m and 0 <= qyy < n and 0 <= qzz < h:
                if l[qzz][qyy][qxx] == 0:
                    l[qzz][qyy][qxx] = 1
                    tomato -= 1
                    answer = qday + 1
                    q.append([qzz,qyy,qxx,qday + 1])
    return answer

to = 0

if tomato != 0:
    to = bfs()
else:
    to = 0

if tomato:
    to = -1

print(to)