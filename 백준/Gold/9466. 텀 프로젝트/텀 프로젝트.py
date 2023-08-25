import sys
sys.setrecursionlimit(10**5)
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = [0] + list(map(int, sys.stdin.readline().split()))
    
    def dfs(now):
        global answer
        check[now] = 1
        rotate.append(now)

        if check[l[now]]:
            if l[now] in rotate:
                answer += rotate[rotate.index(l[now]):]
            return
        else:
            dfs(l[now])

    check = [0] * (n+1)
    answer = []
    for i in range(1,n+1):
        if check[i] == 0:
            rotate = []
            dfs(i)
    print(n - len(answer))