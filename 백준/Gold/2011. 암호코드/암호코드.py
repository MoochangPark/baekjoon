n = list(map(int, input().strip()))
m = len(n)

dp = [0] * (m+1)

dp[0] = 1
dp[1] = 1

if n[0] == 0:
    print(0)
else:
    for i in range(1,m):
        if 0 < n[i]:
            dp[i+1] += dp[i]
        if 10 <= n[i-1]*10 + n[i] <= 26:
            dp[i+1] += dp[i-1]
    print(dp[m] % 1000000)