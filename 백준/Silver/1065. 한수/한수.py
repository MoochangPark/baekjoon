n = int(input())

cnt = 0

for i in range(1,n+1):
    a = list(str(i))
    if len(a) <= 2:
        cnt += 1
    else:
        t = -999999
        check = True
        for j in range(len(a) - 1):
            p = int(a[j]) - int(a[j+1])
            if t == -999999:
                t = p
            else:
                if t != p:
                    check = False
                    break
            
        if check:
            cnt += 1

print(cnt)