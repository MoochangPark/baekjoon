n = int(input())
l = list(map(int, input().split()))

l.sort()
s = 0
e = len(l)-1
answer = [21E8, 21E8]
while s < e:
    if l[s] + l[e] == 0:
        answer = [l[s],l[e]]
        break

    if abs(answer[0] + answer[1]) > abs(l[s] + l[e]):
        answer = [l[s],l[e]]

    if l[s]+l[e] < 0:
        s += 1
    else:
        e -= 1

print(*answer)