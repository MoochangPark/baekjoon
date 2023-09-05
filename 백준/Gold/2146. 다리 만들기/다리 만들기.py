from collections import deque

n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]


def find_land(sy, sx, area):
    q = deque()
    q.append([sy,sx])
    v[sy][sx] = 1
    l[sy][sx] = area
    while q:
        y, x = q.popleft()

        for dy, dx in ((y+1, x),(y-1, x),(y, x+1),(y, x-1)):
            if 0 <= dy < n and 0 <= dx < n and l[dy][dx] == 1 and v[dy][dx] == 0:
                q.append([dy,dx])
                v[dy][dx] = 1
                l[dy][dx] = area

area = 1

for i in range(n):
    for j in range(n):
        if l[i][j] == 1 and v[i][j] == 0:
            find_land(i,j, area)
            area += 1

answer = 21E8

def make_bridge(area):
    global answer
    q = deque()
    dp = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if l[i][j] == area:
                q.append([i,j])
                dp[i][j] = 0
    
    while q:
        y, x = q.popleft()
        for dy, dx in ((y+1, x),(y-1, x),(y, x+1),(y, x-1)):
            if 0 <= dy < n and 0 <= dx < n:
                if l[dy][dx] > 0 and l[dy][dx] != area:
                    answer = min(answer, dp[y][x])
                    return
                if l[dy][dx] == 0 and dp[dy][dx] == -1:
                    q.append([dy,dx])
                    dp[dy][dx] = dp[y][x] + 1
    
for i in range(1,area):
    make_bridge(i)

print(answer)