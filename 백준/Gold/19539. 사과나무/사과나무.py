n = int(input())
l = list(map(int, input().split()))

if sum(l) % 3 == 0:
    # a = 0
    c = 0
    for ll in l:
        # a += (ll // 3)
        c += (ll // 2)

    if sum(l) // 3 <= c:
        print('YES')
    else:
        print('NO')

else:
    print('NO')