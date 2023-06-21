r, c, k = map(int, input().split())

l = []
ch = [[0] * c for _ in range(r)]
for _ in range(r):
    l.append(list(input()))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

cnt = 0

def dfs(rr,cc,kk):
    global r, c, k, cnt
    if kk == k:
        if rr == 0 and cc == c-1:
            cnt += 1
            return
    
    for i in range(4):
        dr = rr + dy[i]
        dc = cc + dx[i]
        if 0 <= dr < r and 0 <= dc < c:
            if l[dr][dc] == '.' and ch[dr][dc] == 0:
                ch[dr][dc] = 1
                dfs(dr, dc, kk+1)
                ch[dr][dc] = 0


ch[r-1][0] = 1
dfs(r-1, 0, 1)

print(cnt)