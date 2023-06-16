N = int(input())

l = []
for _ in range(N):
    l.append(input())

l.sort()
ans = N
for i in range(N):
    ch = True
    for j in range(i, N):
        if i != j:
            t = l[j]
            if l[i] == t[0:len(l[i])]:
                ch = False
                break
    if not ch:
        ans -= 1

print(ans)