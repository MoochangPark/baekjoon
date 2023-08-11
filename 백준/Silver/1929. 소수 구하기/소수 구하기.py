n, m = map(int, input().split())

l = [0,0]+([1] * (m+1))

for i in range(2,m+1):
    if l[i]:
        for j in range(i*2,m+1,i):
            l[j] = 0

for i in range(n,m+1):
    if l[i]:
        print(i)