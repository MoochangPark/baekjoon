import sys
N = int(input())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*(N) for _ in range(N)]

for term in range(1, N):
    for start in range(N):  # 첫행렬 : i, 끝행렬: i+term
        if start + term == N:  # 범위를 벗어나면 무시
            break

        dp[start][start+term] = 21E8  # 지금 계산할 첫행렬과 끝행렬
        
        for t in range(start, start+term):
            dp[start][start+term] = min(dp[start][start+term], dp[start][t]+dp[t+1][start+term] + l[start][0] * l[t][1] * l[start+term][1])

print(dp[0][N-1])