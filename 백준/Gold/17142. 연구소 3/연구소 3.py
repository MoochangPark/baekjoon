from collections import deque
from itertools import combinations

n, m = map(int ,input().split())

l = [list(map(int, input().split())) for _ in range(n)]

virus = []

for i in range(n):
    for j in range(n):
        if l[i][j] == 2:
            virus.append([i,j])

answer = 21E8

def bfs1(bfs):

    q = deque()
    ch = [[-1] * n for _ in range(n)]
    for b in bfs:
        q.append(b)
        ch[b[0]][b[1]] = 0
    
    c = 0

    while q:
        y, x = q.popleft()
        
        for dy, dx in ((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
            if 0 <= dy < n and 0 <= dx < n and l[dy][dx] == 0 and ch[dy][dx] == -1:
                q.append([dy,dx])
                ch[dy][dx] = ch[y][x] + 1

    for i in range(n):
        for j in range(n):
            if l[i][j] == 0 and ch[i][j] == -1:
                return -1
            c = max(c,ch[i][j])
    return c

def bfs2(bfs):

    q = deque()
    ch = [[-1] * n for _ in range(n)]
    for b in bfs:
        q.append(b)
        ch[b[0]][b[1]] = 0
    
    c = 0

    while q:
        y, x = q.popleft()
        
        for dy, dx in ((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
            if 0 <= dy < n and 0 <= dx < n and (l[dy][dx] == 0 or l[dy][dx] == 2) and ch[dy][dx] == -1:
                q.append([dy,dx])
                ch[dy][dx] = ch[y][x] + 1

    for i in range(n):
        for j in range(n):
            if l[i][j] == 0 and ch[i][j] == -1:
                return -1
            c = max(c,ch[i][j])
    return c

for i in combinations(virus,m):
    b = bfs1(i)
    c = bfs2(i)

    if b != -1:
        answer = min(answer, b)
    if c != -1:
        answer = min(answer, c)

if answer == 21E8:
    print(-1)
else:
    print(answer)