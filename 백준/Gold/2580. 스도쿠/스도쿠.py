su = [list(map(int, input().split())) for _ in range(9)]

blank = []

def row(r, y):
    for i in range(9):
        if r == su[y][i]:
            return False
    return True
        
def column(c, x):
    for i in range(9):
        if c == su[i][x]:
            return False
    return True

def rect(r, y, x):
    y = y // 3 * 3
    x = x // 3 * 3
    for i in range(3):
        for j in range(3):
            if r == su[y+i][x+j]:
                return False
    return True

def dfs(count):
    if count == len(blank):
        for i in su:
            print(*i)
        exit()
    
    y = blank[count][0]
    x = blank[count][1]

    for add in range(1,10):
        if row(add, y):
            if column(add, x):
                if rect(add, y, x):
                    su[y][x] = add
                    dfs(count+1)
                    su[y][x] = 0


for i in range(9):
    for j in range(9):
        if su[i][j] == 0:
            blank.append([i,j])

dfs(0)