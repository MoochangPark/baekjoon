l, c = list(map(int, input().split()))

alp = input().split()
alp.sort()

li = [''] * (c + 1)

def dfs(level, moum, zaum, next):
    if level == l:
        if moum >= 1 and zaum >= 2:
            print(''.join(li))
        return

    for i in range(next, len(alp)):
        li[level] = alp[i]
        if alp[i] in ('a','e','i','o','u'):
            dfs(level + 1, moum + 1, zaum, i + 1)
        else:
            dfs(level + 1, moum, zaum + 1, i + 1)

dfs(0,0,0,0)