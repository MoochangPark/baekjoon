x, y = map(int, input().split())

z = (y * 100) // x

ans = 0
l, r = 0, x

if z >= 99: #한번이라도 진 순간 100%가 될 수 없다
    print(-1)
else:
    while l <= r:
        mid = (l + r) // 2
        if z < ((y+mid) * 100) // (x+mid):
            ans = mid
            r = mid-1
        else:
            l = mid + 1

    print(ans)