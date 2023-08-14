t = int(input())

for _ in range(t):
  a,b = map(int, input().split())
  b %= 4
  if b == 0:
    b = 4
  c = (a ** b) % 10
  if c == 0:
    print(10)
  else:
    print(c)