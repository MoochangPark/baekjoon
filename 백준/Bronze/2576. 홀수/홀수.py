l = []
a = 21E8
for _ in range(7):
  b = int(input())
  if b % 2 != 0:
    if a > b:
      a = b
    l.append(b)

if a == 21E8:
  print(-1)
else:
  print(sum(l))
  print(a)