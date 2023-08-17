n = int(input())

l =list(input())

for _ in range(n-1):
  t = list(input())
  for i in range(len(t)):
    if l[i] == '?':
      continue
    else:
      if l[i] != t[i]:
        l[i] = '?'
print(''.join(l))