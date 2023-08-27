n, m = map(int, input().split())

l = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())

    l[a].append(b)
    l[b].append(a)

check = [0] * (n)

answer = 0

def dfs(index, count):
    global answer
    if count == 5:
        answer = 1
        return
    for next in l[index]:
        if check[next] == 0:
            check[index] = 1
            dfs(next, count + 1)
            check[index] = 0

for i in range(n):
    dfs(i, 1)

if answer:
    print(1)
else:
    print(0)