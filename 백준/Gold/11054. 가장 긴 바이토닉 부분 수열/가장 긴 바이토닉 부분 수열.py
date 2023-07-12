n = int(input())

l = list(map(int,input().split()))

lr = l[::-1]
up = [1] * (n+1)
down = [1] * (n+1)
for i in range(n):
    for j in range(i):
        if l[j] < l[i]:
            up[i] = max(up[j]+1, up[i])
        if lr[j] < lr[i]:
            down[i] = max(down[j]+1, down[i])

answer = []
for i in range(n):
    answer.append(up[i] + down[n-1-i] -1)

print(max(answer))