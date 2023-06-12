t = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
maps = []

def bfs(y, x):
   q = [(y,x)]
   maps[y][x] = 0

   while q:
       a, b = q.pop(0)

       for i in range(4):
           nx = a + dx[i]
           ny = b + dy[i]

           if nx < 0 or nx >= n or ny < 0 or ny >= m:
              continue
           
           if maps[nx][ny] == 1:
              q.append((nx,ny))
              maps[nx][ny] = 0



for _ in range(t):
    global m, n, k  # m이 가로 , n이 세로
    n, m, k = map(int, input().split())
    maps = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        maps[x][y] = 1

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)