l = int(input())

s = list(map(int, input().split()))


t = int(input())

if t in s:
    print(0)

else:
    s.append(t)
    s.sort()
    cnt = 0

    n = 0
    m = 0

    for ss in s:
        if ss < t:
            n = ss
        elif ss > t:
            m = ss
            break

    for i in range(n+1, m-1):
        for j in range(i, m):
            if i == j:
                continue
            else:
                if i <= t <= j:
                    cnt += 1
    
    print(cnt)