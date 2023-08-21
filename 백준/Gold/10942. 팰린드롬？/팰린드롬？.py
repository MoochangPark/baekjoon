import sys
n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

dp = [[0] * n for _ in range(n)]

question = int(sys.stdin.readline())

for i in range(n):
    for start in range(n-i):
        end = start + i
        if start == end:
            dp[start][end] = 1
        elif l[start] == l[end]:
            if start +1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

for _ in range(question):
    s,e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])