from collections import deque

n, k = map(int, input().split())

q = deque()

check = [-1] * 100001
q.append([0,n])
check[n] = 0

while q:
    cost, now = q.popleft()
    if now == k:
        print(cost)
        break

    if 0 <= now -1 <= 100000 and check[now-1] == -1:
        check[now-1] = 0
        q.append([cost+1, now-1])
    
    if 0 < now * 2 <= 100000 and check[now*2] == -1:
        check[now*2] = 0
        q.appendleft([cost, now*2])
    
    if 0 <= now + 1 <= 100000 and check[now+1] == -1:
        check[now+1] = 0
        q.append([cost+1, now+1])