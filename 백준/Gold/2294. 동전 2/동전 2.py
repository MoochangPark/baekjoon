n, k = map(int, input().split())

l = []

for i in range(n):
  l.append(int(input()))

check = [100001] * (k+1)
check[0] = 0
for c in l:
  for i in range(c,k+1):
    check[i] = min(check[i], check[i-c] +1)

if check[k] == 100001:
  print(-1)
else:
  print(check[k])