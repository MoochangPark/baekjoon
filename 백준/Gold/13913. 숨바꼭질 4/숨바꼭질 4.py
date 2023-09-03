from collections import deque

n, k = map(int, input().split())
q = deque()

check = [0] * 100001
q.append([n,0,[n]])
check[n] = 1

def bfs():

    if n > k:
        return n-k, [int(x) for x in range(n, k-1, -1)]
    
    while q:
        now, time, l = q.popleft()
        
        if now == k:
            return time, l
        
        for dnow in (now-1, now+1, now*2):
            if 0 <= dnow <= 100000 and check[dnow] == 0:
                check[dnow] = 1
                next = l + [dnow]
                q.append([dnow,time+1,next])
at, al = bfs()
print(at)
print(*al)