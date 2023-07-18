from collections import deque

n, m = map(int, input().split())

indegree = [0] * (n+1) #진입 차수

l = [[] for i in range(n+1)] #간선정보



for _ in range(m):
    a, b = map(int, input().split())
    l[a].append(b) # a 다음에 b가 나와야한다 a -> b
    indegree[b] += 1 # b에는 a가 들어오며 진입차수 증가

def sort():
    answer = []

    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        answer.append(now)

        for i in l[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    print(*answer)
sort()