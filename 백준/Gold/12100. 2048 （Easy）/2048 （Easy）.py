import copy

n = int(input())

l = [list(map(int, input().split())) for i in range(n)]

answer = 0

def up(map):
    for j in range(n):
        p = 0
        for i in range(n):
            if map[i][j] == 0:
                continue
            else:
                t = map[i][j]
                map[i][j] = 0

                if map[p][j] == 0:
                    map[p][j] = t
                elif map[p][j] == t:
                    map[p][j] *= 2
                    p += 1
                else:
                    p += 1
                    map[p][j] = t
    return map

def down(map):
    for j in range(n):
        p = n-1
        for i in range(n-1, -1, -1):
            if map[i][j] == 0:
                continue
            else:
                t = map[i][j]
                map[i][j] = 0

                if map[p][j] == 0:
                    map[p][j] = t
                elif map[p][j] == t:
                    map[p][j] *= 2
                    p -= 1
                else:
                    p -= 1
                    map[p][j] = t
    return map

def left(map):
    for i in range(n):
        p = 0
        for j in range(n):
            if map[i][j] == 0:
                continue
            else:
                t = map[i][j]
                map[i][j] = 0

                if map[i][p] == 0:
                    map[i][p]= t
                elif map[i][p] == t:
                    map[i][p] *= 2
                    p += 1
                else:
                    p += 1
                    map[i][p] = t
    return map

def right(map):
    for i in range(n):
        p = n-1
        for j in range(n-1,-1,-1):
            if map[i][j] == 0:
                continue
            else:
                t = map[i][j]
                map[i][j] = 0

                if map[i][p] == 0:
                    map[i][p]= t
                elif map[i][p] == t:
                    map[i][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    map[i][p] = t
    return map

def dfs(map, count):
    global answer
    if count >= 5:
        t = 0
        for i in range(n):
            for j in range(n):
                if map[i][j] > t:
                    t = map[i][j]
        answer = max(answer, t)
        return
    
    dfs(up(copy.deepcopy(map)),count+1)
    dfs(down(copy.deepcopy(map)),count+1)
    dfs(left(copy.deepcopy(map)),count+1)
    dfs(right(copy.deepcopy(map)),count+1)

dfs(l, 0)
print(answer)