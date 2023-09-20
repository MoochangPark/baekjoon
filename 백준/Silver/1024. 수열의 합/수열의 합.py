n, l = map(int, input().split())

for i in range(l, 101):
  j = n/i - (i+1)/2
  if int(j) == j:
    j = int(j)
    if j +1 >= 0:
      for k in range(j+1, j+i+1):
        print(k, end=" ")
      break
else:
  print(-1)