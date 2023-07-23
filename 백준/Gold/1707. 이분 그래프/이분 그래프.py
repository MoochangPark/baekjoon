from collections import deque

k = int(input())

for _ in range(k):
    answer = True
    v, e = map(int, input().split())

    l = [0] * (v+1)
    d = {}

    for _ in range(e):
        s,b = map(int, input().split())
        if s not in d:
            d[s] = []
        if b not in d:
            d[b] = []
        
        d[s].append(b)
        d[b].append(s)
        
        l[s] = 3
        l[b] = 3

    q = deque()

    def bfs():
        while q:
            me = q.popleft()
            for m in d[me]:
                if l[m] == 3:
                    l[m] = -1 * l[me]
                    q.append(m)
                else:
                    if l[m] == l[me]:
                        return False
        return True


    for ll in range(len(l)):
        if answer:
            if l[ll] == 3:
                l[ll] = 1
                q.append(ll)
                answer = bfs()

    print('YES' if answer else 'NO')