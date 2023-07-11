from collections import deque

n,m = map(int, input().split())

l = [list(map(int, input())) for _ in range(n)]

check = [[[0]*2 for _ in range(m+1)] for _ in range(n+1)]

def bfs():
    
    while q:
        qy, qx, wall = q.popleft()

        if [qy,qx] == [n-1,m-1]:
            print(check[qy][qx][wall])
            return

        for y, x in ((-1,0),(1,0),(0,-1),(0,1)):
            dy = qy + y
            dx = qx + x
            if 0<= dy < n and 0 <= dx < m:
                if l[dy][dx] == 0 and check[dy][dx][wall] == 0:
                    check[dy][dx][wall] = check[qy][qx][wall] + 1
                    q.append([dy, dx, wall])
                elif l[dy][dx] == 1 and wall == 0:
                    check[dy][dx][wall+1] = check[qy][qx][wall] + 1
                    q.append([dy, dx, wall+1])
    print(-1)
    return

q = deque()

check[0][0][0] = 1
q.append([0,0,0])
bfs()