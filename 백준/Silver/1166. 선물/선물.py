n, l, w, h = map(int, input().split())

s, r = 0, max(l, w, h)

for _ in range(10000):
    mid = (s + r) / 2
    cnt = (l // mid) * (w // mid) * (h // mid)
    if cnt >= n:
        s = mid
    else:
        r = mid
    
print('%.10f'%r)