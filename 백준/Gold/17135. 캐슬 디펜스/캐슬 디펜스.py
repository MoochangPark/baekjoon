from itertools import combinations
from copy import deepcopy

n, m, d = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)] + [[2] * m] #1은 적

enemy = []

for i in range(n-1, -1, -1):
    for j in range(m):
        if l[i][j] == 1:
            enemy.append([i,j])

def game(x, e):
    all = len(e)
    catch = 0
    dead = 0

    while dead < all:
        
        #적 찾기
        shot = []
        
        for i in x:
            find = []
            for j in range(len(e)):
                if e[j] != [-1,-1]:
                    array = abs(i[0] - e[j][0]) + abs(i[1] - e[j][1]) #거리
                    if array <= d:
                        find.append((array,e[j][0], e[j][1], j))
            
            find.sort(key=lambda x : (x[0], x[2]))
            if find:
                shot.append(find[0])


        #실제 공격        
        for s in shot:
            if e[s[3]] != [-1,-1]:
                e[s[3]] = [-1,-1]
                catch += 1
                dead += 1

        #적 이동
        for k in range(len(e)):
            if e[k] != [-1,-1]:
                e[k][0] += 1
                if e[k][0] >= n:
                    dead += 1
                    e[k] = [-1,-1]

    return catch

answer = 0
for x in combinations([[n,x] for x in range(m)],3):
    answer = max(answer, game(x, deepcopy(enemy)))

print(answer)