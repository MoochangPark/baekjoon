n, k = map(int, input().split())

l = [True] * n
ans = []
b = n

t = -1 #현위치
cnt = 0 #넘어간 개수
while b > 0:
    t = (t + 1) % n
    if l[t]: cnt += 1
    if cnt == k:
        l[t] = False
        ans.append(t+1)
        cnt = 0
        b -= 1
print(str(ans).replace('[', '<').replace(']', '>'))
    