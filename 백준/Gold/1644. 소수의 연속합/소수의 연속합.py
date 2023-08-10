n = int(input())

che = [0,0] + [1] * (n)
for i in range(2, int(n**0.5) + 1):
    if che[i]:
        for j in range(i*2, n+1, i):
            che[j] = 0

l = []
for i in range(n+1):
    if che[i]:
        l.append(i)

answer = 0
i = 0
j = 0

while j <= len(l):
    sums = sum(l[i:j])
    if sums == n:
        answer += 1
        j += 1
    elif sums < n:
        j += 1
    else:
        i += 1
        
print(answer)
