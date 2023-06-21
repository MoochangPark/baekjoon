t = int(input())

l = []
for _ in range(t):
    a, b = map(int, input().split())
    l.append(b-a)
l.sort()

ans = 0

if len(l) % 2 != 0:
    ans = 1
else:
    t = len(l) // 2 - 1
    ans = l[t + 1] - l[t] + 1

print(ans)

