n, s = map(int, input().split())

l = list(map(int, input().split()))

a, b = 0, 0
answer = 100000
add = l[0]
while a <= b:

    if add >= s:
        answer = min(answer, b - a + 1)
        add -= l[a]
        a += 1
    
    else:
        b += 1
        if b < n:
            add += l[b]
        else:
            break
print(0) if answer == 100000 else print(answer)