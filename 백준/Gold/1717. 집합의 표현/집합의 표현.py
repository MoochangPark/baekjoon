import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n,m = map(int, input().split())

l = [i for i in range(n+1)]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        l[b] = a
    else:
        l[a] = b

def find(c):
    if l[c] != c:
        l[c] = find(l[c])
    return l[c]

for _ in range(m):
    t, a, b = map(int, input().split())

    if t:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a,b)