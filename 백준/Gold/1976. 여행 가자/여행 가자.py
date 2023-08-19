n = int(input())
m = int(input())


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n)]

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(n):
        if t[j] == 1:
            union(parent, i, j)

arr = list(map(int, input().split()))

for i in range(1,m):
    if parent[arr[i]-1] != parent[arr[0]-1]:
        print('NO')
        exit()
print('YES')