n = (int(input()))

l = list(map(int, input().split()))

for p in range(n-1, 0, -1):
  if l[p] > l[p-1]:
    for k in range(n-1, 0, -1):
      if l[p-1] < l[k]:
        l[k], l[p-1] = l[p-1], l[k]
        l = l[:p] + sorted(l[p:])
        print(*l)
        exit() 
print(-1)