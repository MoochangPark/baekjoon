n, m, h = map(int, input().split()) #m은 미리 놓인 선

l = [[0] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    l[a-1][b-1] = 1

answer = 4

def check():
    for i in range(n):
        now = i
        for j in range(h):
            if l[j][now]:
                now += 1
            elif now > 0 and l[j][now-1]:
                now -= 1
        if now != i:
            return False
    return True

def dfs(hh, nn, count):
    global answer

    if count > 3 or count >= answer:
        return
    
    if check():
        answer = min(answer, count)
    
    for i in range(hh, h):
        k = nn if i == hh else 0
        for j in range(k, n-1):
            if l[i][j] == 0:
                l[i][j] = 1
                dfs(i, j+2, count + 1)
                l[i][j] = 0

dfs(0,0,0)

print(answer if answer <= 3 else -1)