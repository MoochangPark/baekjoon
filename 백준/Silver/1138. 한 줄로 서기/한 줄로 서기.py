N = int(input())

h = list(map(int, input().split()))
l = [0] * N
for i in range(N):
    cnt = 0
    for j in range(N):
        if l[j] == 0 and cnt == h[i]:
            l[j] = i + 1
            break
        elif l[j] == 0:
            cnt += 1
print(*l)