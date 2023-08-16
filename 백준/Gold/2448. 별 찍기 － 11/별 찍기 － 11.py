n = int(input())

l = [[' ']* (2 * n) for _ in range(n)]

def dfs(y, x, z):
    if z == 3:
        l[y][x] = '*' #첫번째 1개
        l[y+1][x-1] = '*' #두번째 줄
        l[y+1][x+1] = '*' #두번쨰 줄
        for i in range(-2, 3): #3번쨰 줄
            l[y+2][x+i] = '*'
        return

    zz = z // 2 #사이즈 줄이기
    #n=6일 경우 (0,5), (3,2), (3,8)에서 부터 삼각형을 그려야함
    dfs(y, x, zz)
    dfs(y + zz, x - zz, zz)
    dfs(y + zz, x + zz, zz)

dfs(0, n-1, n) #0 부터 n-1인건 맨 윗 꼭짓점이 중앙에서부터 찍히기 때문

for ll in l:
    print(''.join(ll))