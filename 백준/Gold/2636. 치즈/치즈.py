from collections import deque

n, m = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(n)]

cheese = 0

for i in range(n):
    for j in range(m):
        if l[i][j] == 1:
            cheese += 1

def find_out():
    che = []

    q = deque()
    q.append([0,0])
    ch[0][0] = 1
    while q:
        qy, qx = q.popleft()
        for dy, dx in ((qy+1,qx),(qy-1,qx),(qy,qx+1),(qy,qx-1)):
            if 0 <= dy < n and 0 <= dx < m:
                if ch[dy][dx] == 0:
                    if l[dy][dx] == 0:
                        q.append([dy,dx])
                    else:
                        che.append([dy,dx])
                    ch[dy][dx] = 1

    count = 0
    for y, x in che:
        l[y][x] = 0
        count += 1
    
    return count

t = 1 #공기 첩촉 시간
while True:
    ch = [[0] * (m+1) for _ in range(n)]
    touch = find_out()
    cheese -= touch
    if cheese == 0:
        print(t)
        print(touch)
        break
    t += 1
