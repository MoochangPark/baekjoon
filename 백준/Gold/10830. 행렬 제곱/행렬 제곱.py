import sys
sys.setrecursionlimit(10**5)

n, b = map(int, sys.stdin.readline().split())

l = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        l[i][j] %= 1000

def power(l, b):
    if b == 1:
        return l
    npower = power(l, b//2)
    if b % 2 == 0:
        return calc(npower, npower)
    else:
        return calc(calc(npower, npower), l)

def calc(a, b):
    n = len(a)
    news = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                news[i][j] += a[i][k] * b[k][j]
            news[i][j] %= 1000
    return news

answer = power(l, b)

for i in range(n):
    print(*answer[i])