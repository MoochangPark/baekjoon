n, m = map(int, input().split())

maxs = 0

l = []

for i in range(n):
    t = list(map(int, str(input())))
    l.append(t)

nm = min(n,m)
for i in range(n):
    for j in range(m):
        for k in range(nm):
            if i + k < n and j + k < m:
                if l[i][j] == l[i][j + k] == l[i + k][j] == l[i + k][j + k]:
                    maxs = max(maxs, (k+1) * (k+1))
print(maxs)