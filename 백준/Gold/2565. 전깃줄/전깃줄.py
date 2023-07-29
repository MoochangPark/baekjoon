n = int(input())

l = []

for i in range(n):
    l.append(list(map(int,input().split())))

l.sort(key=lambda x : x[0])

ch = [1] * n

for i in range(1,n):
    for j in range(i):
        if l[j][1] < l[i][1]:
            ch[i] = max(ch[i], ch[j]+1)

print(n - max(ch))