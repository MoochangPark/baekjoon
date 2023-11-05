from collections import Counter

a = Counter(input())
b = Counter(input())

t = (a - b) + (b - a)
answer = 0
for i in t.values():
  answer += i
print(answer)