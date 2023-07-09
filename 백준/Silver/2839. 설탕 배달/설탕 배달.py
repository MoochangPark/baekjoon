n = int(input())
answer = 0
t = n // 5
n %= 5

while t >= 0:

  if n % 3 == 0:
    t += n // 3
    break
  else:
    t -= 1
    n += 5

print(t if t else -1)