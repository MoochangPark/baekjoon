from itertools import combinations
from collections import deque

n, m = map(int, input().split())
maxs = 0

l = []

for _ in range(n):
    l.append(list(map(int, input().split())))


check = []

for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
            check.append([i,j])

def finalCheck(w, c):
    global n, m
    answer = 0
    for i in range(n):
        for j in range(m):
            if c[i][j] != 3 and [i,j] not in w and l[i][j] == 0:
                answer += 1
    return answer

def bfs(wall, checklist):
    global n, m, maxs
    v = deque()
    for i in range(n):
        for j in range(m):
            if l[i][j] == 2:
                v.append([i,j])
    
    while v:
        q = v.popleft()
        for dy, dx in [(0,-1), (0,1), (-1,0), (1,0)]:
            qdy = q[0] + dy
            qdx = q[1] + dx
            if 0 <= qdy < n and 0 <= qdx < m:
                if l[qdy][qdx] != 1 and l[qdy][qdx] != 2 and checklist[qdy][qdx] != 3:
                    if [qdy,qdx] not in wall:
                        checklist[qdy][qdx] = 3
                        v.append([qdy,qdx])

    answer = finalCheck(wall, checklist)
    maxs = max(maxs, answer)

def makeThree():
    for wall in combinations(check, 3):
        checklist = [[0] * m for _ in range(n)]
        bfs(wall, checklist)

makeThree()
print(maxs)