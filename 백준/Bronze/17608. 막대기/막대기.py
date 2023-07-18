n = int(input())

l = []

for _ in range(n):
    ac = int(input())

    while len(l) > 0 and l[-1] <= ac:
        l.pop(-1)
    l.append(ac)

print(len(l))