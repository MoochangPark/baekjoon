n = int(input())

l = []
for i in range(n):
  l.append(input())

for i in range(1, len(l[0])+1):
  check = []
  for j in range(n):
    if l[j][-i:] not in check:
      check.append(l[j][-i:])
    else:
      break
  if len(check) == n:
    print(i)
    break