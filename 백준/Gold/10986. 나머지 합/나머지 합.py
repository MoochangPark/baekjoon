n, m = map(int, input().split())

l = []
arr = list(map(int, input().split()))

sum = [0] * (n+1)
mul = [0] * m

answer = 0

#
sum[0] = arr[0]
for i in range(1,n):
    sum[i] = sum[i-1] + arr[i]

for i in range(n):
    temp = sum[i] % m
    if temp == 0:
        answer += 1
    mul[temp] += 1

for i in range(m):
    if mul[i] > 1:
        answer += (mul[i] * (mul[i]-1)) // 2

print(answer)