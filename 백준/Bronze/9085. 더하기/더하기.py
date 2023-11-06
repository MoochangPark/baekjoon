t = int(input())

for _ in range(t):
  answer = 0
  n = int(input())
  l = list(map(int, input().split()))
  for i in range(n):
    answer += l[i]
  print(answer)