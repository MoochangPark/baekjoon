n = int(input())

l = list(map(int, input().split()))

l.sort()

L = 0
R = n-1
answer = [L,R]
cmp = abs(l[L] + l[R])

while L < R:
    t = l[R] + l[L]
    if abs(t) < cmp:
        answer = [L,R]
        cmp = abs(t)
    if t < 0:
        L += 1
    else:
        R -= 1

print(l[answer[0]], l[answer[1]])