l = list(map(int, input().split()))
i = 1
while True:
  c = 0
  for j in l:
    if i % j == 0:
      c += 1
  if c >= 3:
    print(i)
    break
  i+=1