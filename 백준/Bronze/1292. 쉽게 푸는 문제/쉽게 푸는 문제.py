a,b = map(int,input().split())

l = [0]

for i in range(100):
  for j in range(i):
    l.append(i)
print(sum(l[a:b+1]))