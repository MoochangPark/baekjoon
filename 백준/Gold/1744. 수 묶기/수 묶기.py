from itertools import combinations
n = int(input())

up = []
down = []

answer = 0

for _ in range(n):
    t = int(input())
    if t > 1:
        up.append(t)
    else:
        down.append(t)

up.sort()
down.sort(reverse=True)

while len(up):
    if len(up) == 1:
        break

    a = up.pop()
    b = up.pop()
    answer += (a*b) if (a*b) > (a+b) else (a+b)

if len(up):
    answer += up.pop()

while len(down):
    if len(down) == 1:
        break

    a = down.pop()
    b = down.pop()
    answer += (a*b) if (a*b) > (a+b) else (a+b)

if len(down):
    answer += down.pop()

print(answer)