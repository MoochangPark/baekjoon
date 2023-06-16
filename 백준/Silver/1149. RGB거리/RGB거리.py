n = int(input())

l = [[0] * 3 for _ in range(n+1)] #빨, 초, 파

for i in range(n):
    l[i][0], l[i][1], l[i][2] = map(int, input().split())


for i in range(1,n):
    l[i][0] = l[i][0] + min(l[i-1][1], l[i-1][2])
    l[i][1] = l[i][1] + min(l[i-1][0], l[i-1][2])
    l[i][2] = l[i][2] + min(l[i-1][0], l[i-1][1])

print(min(l[n-1]))