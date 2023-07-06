from itertools import combinations

n, m = map(int, input().split())

l = [[0] * (n+1) for _ in range(n+1) ]

house = []
store = []

answer = 21E8

for i in range(1,n+1):
    t = list(map(int, input().split()))
    for j in range(len(t)):
        if t[j] == 1:
            house.append([i,j])
        elif t[j] == 2:
            store.append([i,j])

def find_via_house(e):
    all_sum = 0
    for h in house:
        road = 21E8
        for es in e:
            length = abs(h[0] - es[0]) + abs(h[1] - es[1])
            road = min(road, length)
        all_sum += road
    return all_sum

for mx in range(1,m+1):
    for e in combinations(store,mx):
        fvh = find_via_house(e)
        answer = min(answer, fvh)

print(answer)