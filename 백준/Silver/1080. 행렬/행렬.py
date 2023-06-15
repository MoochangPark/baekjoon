n, m = map(int, input().split())

l = []
r = []

cnt = 0

for _ in range(n):
    l.append( list( map(int, list(input()) ) ) )

for _ in range(n):
    r.append( list( map(int, list(input()) ) ) )


def change(y,x):
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            l[i][j] = 1 - l[i][j]

for y in range(n - 2):
    for x in range(m - 2):
        if l[y][x] != r[y][x]:
            change(y,x)
            cnt += 1

ch = True
for y in range(n):
    for x in range(m):
        if l[y][x] != r[y][x]:
            ch = False
            break


if ch:
    print(cnt)
else:
    print(-1)