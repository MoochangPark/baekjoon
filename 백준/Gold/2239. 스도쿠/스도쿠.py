board = [list(map(int, input())) for _ in range(9)]
zero = []
answer = []
tag = False

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero.append([i,j])

def row(y,i):
    for j in range(9):
        if board[y][j] == i:
            return False
    return True

def column(x,i):
    for j in range(9):
        if board[j][x] == i:
            return False
    return True

def square(sy,sx,i):
    for j in range(sy,sy+3):
        for k in range(sx,sx+3):
            if board[j][k] == i:
                return False
    return True

def dfs(p):
    global tag
    
    if p == len(zero):
        for i in range(9):
            print(''.join(map(str,board[i])))
        tag = True
        return

    y, x = zero[p]
    
    sy, sx = (y//3)*3, (x//3)*3
    
    for i in range(1,10):
        a = row(y,i)
        if not a:
            continue
        b = column(x,i)
        if not b:
            continue
        c = square(sy,sx,i)
        if not c:
            continue

        board[y][x] = i
        dfs(p+1)
        board[y][x] = 0
        
        if tag:
            return

dfs(0)