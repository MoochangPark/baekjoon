n, s = map(int, input().split())


l = list(map(int, input().split()))
ch = [0] * n
ss = []
cnt = 0

def dfs(m, sm):
    global n, s, cnt
    if m >= n:
        return
    
    sm += l[m]

    if sm == s:
        cnt += 1

    dfs(m+1, sm - l[m])
    dfs(m+1, sm)

dfs(0,0)

print(cnt)