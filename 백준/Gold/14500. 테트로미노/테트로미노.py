
n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def mount(i,j):
    global answer
    t = [(0,1),(0,-1),(1,0),(-1,0)]
    for k in range(4):
        add = l[i][j]
        for u in range(4):
            if u != k:
                if 0<=i+t[u][0]<n and 0<=j+t[u][1]<m:
                    add += l[i+t[u][0]][j+t[u][1]]
        answer = max(answer,add)

check = [[0] * (m+1) for _ in range(n + 1)]

def dfs(qy, qx, count, sum):
    global answer

    if count == 4:
        answer = max(answer, sum)
        return
    
    for y, x in ((0,1),(0,-1),(1,0),(-1,0)):
        dy = qy + y
        dx = qx + x

        if 0 <= dy < n and 0 <= dx < m:
            if check[dy][dx] == 0:
                if count + 1 <= 4:
                    check[dy][dx] = 1
                    dfs(dy, dx, count + 1, sum + l[dy][dx])
                    check[dy][dx] = 0
                

for i in range(n):
    for j in range(m):
        check[i][j] = 1
        dfs(i,j,1,l[i][j])
        mount(i,j)
        check[i][j] = 0
print(answer)