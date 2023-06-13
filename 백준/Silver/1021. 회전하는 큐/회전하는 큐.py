from collections import deque

n,m = map(int, input().split())
l = list(map(int, input().split()))

t = []

cnt = 0

for i in range(1, n+1):
    t.append(i)

while len(l):
    p = l.pop(0)
    while t[0] != p:
        if t.index(p) <= len(t) // 2:
            a = t.pop(0)
            t.append(a)
            cnt += 1
        else:
            a = t.pop(-1)
            t.insert(0,a)
            cnt += 1

    t.pop(0) #제거

print(cnt)