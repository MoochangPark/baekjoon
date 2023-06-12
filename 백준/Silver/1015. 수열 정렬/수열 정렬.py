n = int(input())

l = list(map(int, input().split()))

t = []
for idx, x in enumerate(l):
    t.append((idx, x))

t = sorted( t, key = lambda x: (x[1], x[0]) )

b = [-1] * len(t)
k = 0

for i in t:
    b[i[0]] = k
    k+=1

print(*b)