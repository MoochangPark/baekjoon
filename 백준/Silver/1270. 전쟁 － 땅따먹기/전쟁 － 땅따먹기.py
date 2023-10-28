t = int(input())

for _ in range(t):
  l = list(map(int, input().split()))
  a = l[0]
  b = l[1:]
  
  mid = a // 2
  d = {}
  an = set()
  for i in b:
    if i in d:
      d[i] += 1
      if d[i] > mid:
        an.add(i)
    else:
      d[i] = 1

  if len(an) == 1:
    print(list(an)[0])
  else:
    print("SYJKGW")
  