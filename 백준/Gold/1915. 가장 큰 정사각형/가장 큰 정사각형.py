n, m = map(int, input().split())

l = [list(map(int,input())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = l[i][j]

        elif l[i][j] == 0:
            dp[i][j] = 0

        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        answer = max(answer, dp[i][j])

print(answer * answer)