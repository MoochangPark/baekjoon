l = input()
for i in range(len(l)):
  a = l[i:]
  b = l[i:][::-1]

  if a == b:
    print(len(l)+i)
    break