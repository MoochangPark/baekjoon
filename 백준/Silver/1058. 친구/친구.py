n = int(input())
g = [list(input()) for _ in range(n)]
l = [[0]*n for _ in range(n)]

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i != j and (g[i][j] == 'Y' or (g[i][k] == 'Y' and g[k][j] == 'Y')):
        l[i][j] = 1

answer = 0
for gg in l:
  answer = max(answer, sum(gg))

print(answer)