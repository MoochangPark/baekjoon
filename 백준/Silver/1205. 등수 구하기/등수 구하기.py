n, te, p = map(int, input().split())

if n:
    l = list(map(int, input().split()))
else:
    l = []

l.append(te)

l.sort(reverse=True)

if n == 0:
    print(1)
else:
    if n == p and l[-1] >= te:
        print(-1)
    else:
        t = 0
        s = 0
        for i in range(len(l)):
            if l[i] < te:
                t += s
                break
            elif l[i] > te:
                t += 1
            else:
                if l[i] != te:
                    s += 1
                continue
        print(t+1)