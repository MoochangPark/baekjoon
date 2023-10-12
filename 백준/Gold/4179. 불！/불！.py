from collections import deque
r, c = map(int, input().split())

l = [list(input()) for _ in range(r)]

q = deque()
for i in range(r):
    for j in range(c):
        if l[i][j] == 'J':
            q.append([0,i,j])

for i in range(r):
    for j in range(c):
        if l[i][j] == 'F':
            q.append([-1,i,j])

answer = "IMPOSSIBLE"

while q:
    t, y, x = q.popleft()

    if t > -1 and l[y][x] != 'F' and (y == 0 or x == 0 or y == r-1 or x == c-1):
            answer = t + 1
            break
    
    for d in ((-1,0),(1,0),(0,-1),(0,1)):
        dy = y + d[0]
        dx = x + d[1]

        if 0 <= dy < r and 0 <= dx < c and l[dy][dx] != '#':

                if t > -1 and l[dy][dx] == '.':
                    l[dy][dx] = ','
                    q.append([t+1, dy, dx])
                
                elif t == -1 and l[dy][dx] != 'F':
                    l[dy][dx] = 'F'
                    q.append([-1, dy, dx])

print(answer)