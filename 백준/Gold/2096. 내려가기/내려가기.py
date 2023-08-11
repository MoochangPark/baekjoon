import copy
n= int(input())

l = list(map(int, input().split()))

maxs = copy.deepcopy(l)
mins = copy.deepcopy(l)

for _ in range(1,n):
    t = list(map(int, input().split()))
    maxs = [t[0] + max(maxs[0], maxs[1]), t[1] + max(maxs), t[2] + max(maxs[1], maxs[2])]
    mins = [t[0] + min(mins[0], mins[1]), t[1] + min(mins), t[2] + min(mins[1], mins[2])]

print(max(maxs), min(mins))