n, m = map(int, input().split())

l = [list(map(int,input().split())) for _ in range(n)]

check = [[-1] * (m+1) for _ in range(n+1)]

end = [n-1, m-1]

def dfs(y,x, high):
    
    if [y,x] == end:
        return 1
    if check[y][x] != -1:
        return check[y][x]

    count = 0    
    for ny, nx in [(y+1,x),(y,x+1),(y-1,x),(y,x-1)]:
        if 0 <= ny < n and 0 <= nx < m:
            if l[ny][nx] < high:
                count += dfs(ny,nx, l[ny][nx])
    check[y][x] = count
    return check[y][x]

print(dfs(0,0,l[0][0]))