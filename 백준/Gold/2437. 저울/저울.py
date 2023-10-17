n = int(input())
l = list(map(int, input().split()))

l.sort()

answer = 1

for i in l:
     if answer < i:
          break
     else:
          answer += i

print(answer)