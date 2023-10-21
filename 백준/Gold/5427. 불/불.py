from collections import deque

t = int(input())


for _ in range(t):
    answer = 'IMPOSSIBLE'

    w, h = map(int, input().split())
    l = [list(map(str,input())) for _ in range(h)]

    q = deque()

    
    for i in range(h):
        for j in range(w):
            if l[i][j] == '*':
                q.append([-1,i,j])                
    for i in range(h):
        for j in range(w):
            if l[i][j] == '@':
                q.append([0,i,j])                

    while q:
        c,y,x = q.popleft()

        if c > -1  and (y == 0 or x == 0 or y == h-1 or x == w-1):
            answer = c+1
            break

        for dy,dx in ([y+1,x],[y-1,x],[y,x+1],[y,x-1]):
            if 0 <= dy < h and 0 <= dx < w and l[dy][dx] != '#':
                if c > -1 and l[dy][dx] == '.':
                    l[dy][dx] = ','
                    q.append([c+1,dy,dx])

                elif c == -1 and l[dy][dx] != '*':
                    l[dy][dx] = '*'
                    q.append([-1,dy,dx])

    print(answer)