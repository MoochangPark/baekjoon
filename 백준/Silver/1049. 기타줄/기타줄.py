n, m = map(int, input().split())

mins = 99999

p1 = []
p2 = []

for i in range(m):
    a, b = map(int, input().split())
    p1.append(a)
    p2.append(b)

for i in p1:
    for j in p2:
        a, b = i, j
        if 6 > n:
            t1 = a
        else:
            t1 = a * (n//6) if n % 6 == 0 else a * (n//6) + a
        t2 = b*n
        t3 = a * (n//6) + b * (n % 6)
        t = [t1, t2, t3]
        c = min(t)
        mins = min(mins,c)

print(mins)