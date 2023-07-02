n, k = map(int, input().split())

l = [[0,0]]

for _ in range(n):
    w, v = map(int, input().split())
    l.append([w,v])

backpack = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        w = l[i][0]
        v = l[i][1]

        if j < w: #지금 들고 있는 무게보다 작은 값들은 계산할게 아니니까 그대로 가져온다.
            backpack[i][j] = backpack[i-1][j]
        else: #만약 내 무게 차례 이상부터는...
            backpack[i][j] = max(backpack[i-1][j], backpack[i-1][j-w] + v)

print(backpack[n][k]) 