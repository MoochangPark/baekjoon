from collections import deque

m,n = map(int, input().split())

l = []

t = 1
start = []
end = []
item = []
for i in range(n):
  ll = list(map(str,input()))
  for j in range(m):
    if ll[j] == 'S':
      start = [i,j]
    elif ll[j] == 'X':
      ll[j] = str(t)
      item.append([i,j])
      t+=1
    elif ll[j] == 'E':
      end = [i,j]
  l.append(ll)

item.insert(0, start)
item.append(end)

l[start[0]][start[1]] = str(0)
l[end[0]][end[1]] = str(t)

matrix = [[0] * len(item) for _ in range(len(item))]

def bfs(start):
  check = [[0] * m for _ in range(n)]
  while q:
    qy, qx, cnt = q.popleft()
    check[qy][qx] = 1
    if [qy,qx] in item:
      matrix[start][int(l[qy][qx])] = cnt

    for y, x in ((1,0),(0,1),(-1,0),(0,-1)):
      qyy = qy + y
      qxx = qx + x
      if 0 <= qyy < n and 0 <= qxx < m:
        if check[qyy][qxx] != 1 and l[qyy][qxx] != '#':
          check[qyy][qxx] = 1
          q.append([qyy, qxx, cnt + 1])

q = deque()
for i in range(t+1):
  q.append([item[i][0], item[i][1], 0])
  bfs(i)

mins = 21E8

def dfs(start, road, t):
  global mins, item
  if start == len(item) - 1:
    if len(t) == len(item):
      mins = min(mins, road)
      return
    else:
      return
  
  for i in range(len(item)):
    if i not in t:
      dfs(i, road + matrix[start][i], t +[i])

dfs(0, 0, [])
print(mins)