import sys
sys.setrecursionlimit(10**5)

n = int(input())

dic = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())

    dic[a].append([b,c])
    dic[b].append([a,c])

def dfs(node, cost):
    for i in dic[node]:
        nextNode, nextCost = i
        if l[nextNode] == -1:
            l[nextNode] = cost + nextCost
            dfs(nextNode, cost+nextCost)

l = [-1] * (n+1)
l[1] = 0
dfs(1,0)

d = l.index(max(l))
l = [-1] * (n+1)
l[d] = 0
dfs(d,0)

print(max(l))