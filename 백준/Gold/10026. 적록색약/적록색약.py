from collections import deque

n = int(input())

l = []

ch = [[[0,0]] * n for _ in range(n)]

for i in range(n):
    lt = list(input())
    l.append(lt)

q = deque()

yes = 0
no = 0

def bfs(q):
    global yes, no

    while q:
        qy, qx, color = q.popleft()
        for y, x in ((-1,0), (1,0), (0,-1), (0,1)):
            qyy = qy + y
            qxx = qx + x
            if 0 <= qyy < n and 0 <= qxx < n:
                if  ch[qyy][qxx] == [0,0]:
                    if l[qyy][qxx] == color:
                        ch[qyy][qxx] = [no, yes]
                        q.append([qyy,qxx,l[qyy][qxx]])

for i in range(n):
    for j in range(n):
        if ch[i][j] == [0,0]:
            q.append([i,j,l[i][j]])
            no += 1
            ch[i][j] = [no,yes]
            bfs(q)

for i in range(n):
    for j in range(n):
        if l[i][j] == 'G':
            l[i][j] = 'R'
ch = [[[0,0]] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if ch[i][j] == [0,0]:
            q.append([i,j,l[i][j]])
            yes += 1
            ch[i][j] = [no,yes]
            bfs(q)

print(no, yes)