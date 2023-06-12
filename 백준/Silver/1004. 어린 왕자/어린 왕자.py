n = int(input())
for _ in range(n):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    p = int(input())
    for _ in range(p):
        cx, cy, r = map(int, input().split())
        ds = ((x1 - cx) ** 2) + ((y1 - cy) ** 2)
        de = ((x2 - cx) ** 2) + ((y2 - cy) ** 2)
        cr = r ** 2

        if ds < cr and de < cr:
            continue
        elif ds < cr:
            cnt += 1
        elif de < cr:
            cnt += 1
    print(cnt)
