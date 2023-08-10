from collections import deque

v = int(input())

l = [[] for _ in range(v+1)]

for _ in range(v):
    t = list(map(int, input().split()))

    for j in range(1,len(t)-1,2):
        a, b = t[j:j+2]
        l[t[0]].append([a,b])

answer = 0

ch = [-1] * (v+1)

def dfs(start, sum):

    for a, b in l[start]:
        if ch[a] == -1:
            ch[a] = b + sum
            dfs(a,b+sum)

ch[1] = 1
dfs(1,0)

sl = ch.index(max(ch))
ch = [-1] * (v+1)
ch[sl] = 1
dfs(sl,0)

print(max(ch))
