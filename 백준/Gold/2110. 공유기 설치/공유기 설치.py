n, m = map(int, input().split())

l = []

for _ in range(n):
    l.append(int(input()))

l.sort()

s, e = 1, l[-1] - l[0]

answer = 0


while(s <= e):
    mid = (s + e) // 2

    count = 1
    router = l[0]
    
    for i in range(1,n):
        if l[i] >= router + mid:
            count += 1
            router = l[i]
    if count >= m:
        s = mid + 1
        answer = mid
    else:
        e = mid - 1
print(answer)