import sys

n = int(input())
sys.setrecursionlimit(10**5)

l = [list(map(int, input().split())) for _ in range(n)]
dic = [[0] * n for _ in range(n)]

def dfs(sy, sx):
    if dic[sy][sx]:
        return dic[sy][sx]
    dic[sy][sx] = 1
    for dy, dx in ((sy+1,sx),(sy-1,sx),(sy,sx+1),(sy,sx-1)):
        if 0 <= dy < n and 0 <= dx < n: #맵 범위 안에 있고,#뱅글 돌지 않게 간적 없는 경로여야하고,
            if l[sy][sx] < l[dy][dx]: #전 지역보다 옮긴 지역이 더 많아야한다.
                dic[sy][sx] = max(dic[sy][sx],dfs(dy,dx)+1)
    return dic[sy][sx]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i,j))

print(answer)