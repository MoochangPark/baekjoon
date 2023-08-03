import copy

n, m = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(n)]

d = [(-1,0), (0,1), (1,0), (0,-1)]
dir = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    [[0,1,2,3]]
    ]

ch = [[0] * m for _ in range(n)]

cctv = []

for i in range(n):
    for j in range(m):
        if 1<=l[i][j]<=5:
            cctv.append([i,j,l[i][j]])

answer = 21E8

def search(tmp, y, x, rota):
    for k in rota:
        dy = y
        dx = x
        while True:
            dy += d[k][0]
            dx += d[k][1]

            if 0 <= dy < n and 0 <= dx < m:
                if tmp[dy][dx] == 6:
                    break
                elif tmp[dy][dx] == 0:
                    tmp[dy][dx] = 7
            else:
                break

def dfs(count, board):
    global answer
    if count == len(cctv):
        c = 0
        for i in range(n):
            c += board[i].count(0)
        answer = min(answer, c)
        return
    
    tmp = copy.deepcopy(board)
    y, x, ctv = cctv[count]
    for rota in dir[ctv]:
        search(tmp, y, x, rota)
        dfs(count + 1, tmp)
        tmp = copy.deepcopy(board)

dfs(0,l)
print(answer)