n, m = map(int, input().split())

l = [list(input()) for _ in range(n)]
a = 0
b = 0

for i in range(n):
  if 'X' not in l[i]:
    a += 1
    
for i in range(m):
  check = True
  for j in range(n):
    if 'X' in l[j][i]:
      check = False
  if check:
    b += 1
print(max(a,b))