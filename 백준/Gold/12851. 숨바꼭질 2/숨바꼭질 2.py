from collections import deque

n, k = map(int, input().split())

def bfs():
    v = [0] * 100001
    q = deque()

    q.append([n,0])
    answer = 21E8
    count = 0
    while q:

        now, time = q.popleft()

        if now == k:
            if answer == time:
                count += 1
            else:
                answer = min(answer,time)
                count = 1
            continue

        if 0 <= now * 2 < 100001 and (v[now * 2] == 0 or v[now * 2] == time + 1):
            v[now * 2] = time + 1
            q.append([now * 2, time + 1])
        if 0 <= now + 1 < 100001 and(v[now + 1] == 0 or v[now + 1] == time + 1):
            v[now + 1] = time + 1
            q.append([now + 1, time + 1])
        if 0 <= now - 1 < 100001 and (v[now - 1] == 0 or v[now - 1] == time + 1):
            v[now - 1] = time + 1
            q.append([now - 1, time + 1])
        
    return [answer, count]
    

a, b = bfs()

print(a)
print(b)