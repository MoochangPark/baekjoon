# 1위, 2아래, 3오른, 4왼
import sys

n, m, b = map(int, sys.stdin.readline().split()) #세로, 가로, 상어 수

l = [[[] for _ in range(m)] for _ in range(n)]

dr = [[],[-1,0],[1,0],[0,1],[0,-1]]

shark = []

answer = 0

for _ in range(b):
    y, x, s, d, z = map(int, sys.stdin.readline().split()) #y, x, 속력, 이동방향, 크기
    l[y-1][x-1].append([s,d,z])

for p in range(m):
    
    #낚시꾼 낚시
    for i in range(n):
        if l[i][p]:
            a,b,c = l[i][p].pop()
            answer += c
            break
 
    #상어들 이동
    for i in range(n):
        for j in range(m):
            if l[i][j]:
                a,c,d = l[i][j].pop()
                shark.append([i,j,a,c,d])

    while shark:
        y, x, a, c, d = shark.pop()
        cnt = a % ((n-1) * 2) if c == 1 or c == 2 else a % ((m-1) * 2)
        while cnt > 0:
            dy, dx = y + dr[c][0], x + dr[c][1]

            if 0 <= dy < n and 0 <= dx < m:
                y, x = dy, dx
                cnt -= 1

            else:
                if c in [1,3]:
                    c += 1
                elif c in [2,4]:
                    c -= 1
                continue

        l[y][x].append([a,c,d])

    #맵 복사
    for i in range(n):
        for j in range(m):
            if len(l[i][j]) >= 2:
                l[i][j].sort(key=lambda x : -x[2])
                while len(l[i][j]) > 1:
                    l[i][j].pop()

print(answer)