n, k = map(int, input().split())
l = []

for i in range(n):
    l.append(int(input()))

answer = 0

for i in range(n-1,-1,-1):
    answer += k // l[i]
    k %= l[i]

print(answer)