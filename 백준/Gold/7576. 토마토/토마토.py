from collections import deque

n, m = map(int, input().split())
l = []

x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]

def bfs():
    maxs = 0    
    while q:
        qi, qj, qc = q.popleft()

        for i in range(4):
            dqi = qi + x[i]
            dqj = qj + y[i]

            if 0 <= dqi < m and 0 <= dqj < n and l[dqi][dqj] == 0 and l[dqi][dqj] != -1:
                l[dqi][dqj] = 1
                q.append([dqi,dqj,qc+1])
                maxs = qc + 1
    return maxs

for i in range(m):
    l.append(list(map(int, input().split())))

q = deque()

for i in range(m):
    for j in range(n):
        if l[i][j] == 1:
            q.append([i,j,0])

answer = bfs()

for i in range(m):
    for j in range(n):
        if l[i][j] == 0:
            answer = -1
            break
    if answer == -1:
        break

print(answer)