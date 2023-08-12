n= int(input())

l = list(map(int, input().split()))

delt = int(input())

answer = 0

def dfs(dt):
    l[dt] = -2
    for i in range(n):
        if dt == l[i]:
            dfs(i)

dfs(delt)

for i in range(n):
    if l[i] != -2 and (i not in l):
        answer += 1

print(answer)