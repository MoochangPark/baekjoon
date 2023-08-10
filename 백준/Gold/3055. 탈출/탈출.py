from collections import deque

n, m = map(int, input().split())

l = [list(input()) for _ in range(n)]

ch = [[0] * (m+1) for _ in range(n+1)]

ddy = 0
ddx = 0
q = deque()

def dfs(ddY,ddX):
    while q:
        qy, qx = q.popleft()
        if l[ddY][ddX] == 'S':
            return ch[ddy][ddx]
            
        for dy, dx in ((qy+1,qx),(qy-1,qx),(qy,qx+1),(qy,qx-1)):
            if 0 <= dy < n and 0 <= dx < m:
                if (l[dy][dx] == '.' or l[dy][dx] == 'D') and l[qy][qx] == 'S':
                    l[dy][dx] = 'S'
                    ch[dy][dx] = ch[qy][qx] + 1
                    q.append([dy,dx])
                
                elif (l[dy][dx] == '.' or l[dy][dx] == 'S') and l[qy][qx] == '*':
                    l[dy][dx] = '*'
                    q.append([dy,dx])
    return "KAKTUS"

for i in range(n):
    for j in range(m):
        if l[i][j] == 'D':
            ddy,ddx = i, j
        elif l[i][j] == 'S':
            q.append([i,j])

for i in range(n):
    for j in range(m):
        if l[i][j] == '*':
            q.append([i,j])

print(dfs(ddy,ddx))