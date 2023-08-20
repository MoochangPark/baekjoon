from collections import deque

n, m = map(int, input().split())

l = [list(input()) for _ in range(n)]

def bfs(sy, sx):
    q = deque()
    check = [[0] * (m+1) for _ in range(n+1)]
    q.append([sy,sx])
    check[sy][sx] = 1
    count = 0
    while q:
        qy, qx = q.popleft()

        for dy, dx in ((qy+1, qx),(qy-1, qx),(qy, qx+1),(qy, qx-1)):
            if 0 <= dy < n and 0 <= dx < m:
                if l[dy][dx] == 'L' and check[dy][dx] == 0:
                    check[dy][dx] = check[qy][qx] + 1
                    count = max(count, check[dy][dx])
                    q.append([dy,dx])
    return count - 1

answer = 0

for i in range(n):
    for j in range(m):
        if l[i][j] == 'L':
            answer = max(answer, bfs(i,j))
print(answer)