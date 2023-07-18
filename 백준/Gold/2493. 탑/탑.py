n = int(input())

l = list(map(int, input().split()))

check = []
answer = []

for i in range(len(l)):
    while check:
        if check[-1][1] < l[i]:
            check.pop()
        else:
            answer.append(check[-1][0] + 1)
            break
    if not check:
        answer.append(0)
    check.append([i, l[i]])
print(*answer)