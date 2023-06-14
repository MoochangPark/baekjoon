n, k, m = map(int, input().split())

rnd = 0

while k != m:
    if k <= 0 or m <= 0:
        rnd = -1
        break
    k -= k // 2
    m -= m // 2
    rnd += 1
print(rnd)