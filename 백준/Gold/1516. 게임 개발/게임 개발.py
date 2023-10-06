from collections import deque

n = int(input())

l = [0] * (n+1)
t = [0] * (n+1)
g = [[] for _ in range(n+1)]

answer = [0] * (n+1)

q = deque()

for i in range(1,n+1):
    m = list(map(int, input().split()))[:-1]
    t[i] = m[0]
    
    for j in m[1:]:
        g[j].append(i)
        l[i] += 1
    
for i in range(1, n+1):
    if l[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    answer[now] += t[now]

    for i in g[now]:
        l[i] -= 1
        answer[i] = max(answer[i], answer[now])
        if l[i] == 0:
            q.append(i)
    
for i in range(1, n+1):
    print(answer[i])
