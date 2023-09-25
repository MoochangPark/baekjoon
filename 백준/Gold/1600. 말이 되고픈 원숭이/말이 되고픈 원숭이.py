from collections import deque

k = int(input())
w,h = map(int, input().split())

#0은 평지, 1은 장애물
l = [list(map(int, input().split())) for _ in range(h)]
ch = [[[-1] * (k+1) for _ in range(w)] for _ in range(h)]

#12가지 방향
my = [-1,-2,-2,-1,1,2,2,1,-1,1,0,0]
mx = [-2,-1,1,2,2,1,-1,-2,0,0,-1,1]

def bfs():
    q = deque()
    q.append([0,0,0])
    ch[0][0][0] = 0
    
    while q:
        qy, qx, count = q.popleft()

        if qy == h-1 and qx == w-1:
            continue

        for i in range(12):
            y = qy+my[i]
            x = qx+mx[i]
            if 0 <= y < h and 0 <= x < w and l[y][x] == 0:
                if 0 <= i <= 7:
                    if count + 1 <= k and ch[y][x][count+1] == -1:
                        ch[y][x][count+1] = ch[qy][qx][count] + 1 
                        q.append([y,x, count+1])
                else:
                    if ch[y][x][count] == -1:
                        ch[y][x][count] = ch[qy][qx][count] + 1 
                        q.append([y,x, count])
    answer = 21E8
    for i in range(k+1):
        if ch[h-1][w-1][i] != -1:
            answer = min(answer, ch[h-1][w-1][i])
    if answer != 21E8:
        return answer
    else:
        return -1

print(bfs())