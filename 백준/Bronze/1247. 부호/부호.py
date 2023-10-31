for _ in range(3):
  n = int(input())
  a  = 0
  for _ in range(n):
    a += int(input())
  if a == 0:
    print(0)
  elif a > 0:
    print('+')
  else:
    print('-')