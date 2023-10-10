n = int(input())

d = [0] * 26

for _ in range(n):
  na = input()
  t = ord(na[0]) - ord('a')
  d[t] += 1

answer = ''

for i in range(26):
  if d[i] >= 5:
    answer = answer + chr(i + ord('a'))
    
if len(answer) != 0:
  print(answer)
else:
  print('PREDAJA')