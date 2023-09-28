min, max = map(int, input().split())

l = [True] * (max-min+1)

for i in range(2, int(max**0.5)+1):
    t = i*i
    while t <= max:
        s = int(min/t) * t
        for j in range(s, max+1, t):
            if j < min:
                continue
            if l[j-min]:
                l[j-min] = False
        t *= i

answer = 0

for i in l:
    if i:
        answer += 1

print(answer)