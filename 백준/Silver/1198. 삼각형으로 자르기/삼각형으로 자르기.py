from itertools import combinations

n = int(input())

l =[]

for i in range(n):
    l.append(list(map(int, input().split())))

maxs = 0

for cb in combinations(l, 3):

    d = 0
    u = 0

    for i in range(2):
        d += cb[i][0] * cb[i+1][1]
        u += cb[i+1][0] * cb[i][1] 

    d += cb[2][0] * cb[0][1]
    u += cb[0][0] * cb[2][1]

    sm = abs(d - u) /2
    maxs = max(maxs, sm)

print(maxs)