t = int(input())

def dfs(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

for _ in range(t):
    left, right = map(int, input().split())
    bridge = dfs(right) // (dfs(right - left) * dfs(left))
    print(bridge)