from collections import deque

t = int(input())

def bfs():
    global sy,sx,ey,ex

    q = deque()

    q.append([sy,sx])
    while q:
        y, x = q.popleft()

        if abs(y - ey) + abs(x - ex) <= 1000:
            print("happy")
            return()
        
        for i in range(n):
            if v[i] == 0:
                dy, dx = pyon[i]
                if abs(dy - y) + abs(dx - x) <= 1000:
                    q.append([dy,dx])
                    v[i] = 1
    print("sad")
    return

for _ in range(t):
    n = int(input())
    sy, sx = map(int, input().split())
    pyon = [list(map(int, input().split())) for _ in range(n)]
    ey, ex = map(int, input().split())
    v = [0] * (n+2) #시작점, 편의점들, 도착점
    bfs()
    