n = int(input())
l = []

for _ in range(n):
    x, y = map(int, input().split())
    l.append([x,y])
l.append([l[0][0], l[0][1]])

up = 0
down = 0
for i in range(n):
    up += (l[i][0] * l[i+1][1])
    down += (l[i][1] * l[i+1][0])

temp = abs(up-down)

temp /= 2

temp = round(temp,1)

print(temp)