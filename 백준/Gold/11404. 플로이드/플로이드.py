n = int(input())
m = int(input())

cost = [[21E8] * n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c) #최소비용 우선 저장

#플로이드 와셜
for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for row in cost:
    for i in range(n):
        if row[i] == 21E8:
            row[i] = 0
        print(row[i], end=' ')
    print()