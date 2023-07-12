n = int(input()) # 맵 크기
ch = [[0] * n for _ in range(n)] # 체크 맵 생성
k = int(input()) # 사과의 개수
ap = [list(map(int, input().split())) for _ in range(k)] #사과의 위치 받기
l = int(input()) # 방향 전환 수
lp = [list(map(str, input().split())) for _ in range(l)] #방향 전환 시점 받기

dir = [[0,1],[1,0],[0,-1],[-1,0]] # 1우 2하 3좌 4상
d = 0 #현재 방향
snake = [[0,0]] #뱀의 현 바디 상황
ch[0][0] = 1 #현재 뱀 위치를 바로 기록

t = 0 # 시간

x, c = lp.pop(0) # X 초 후에 C 방향으로 회전

while True: #방향 전환을 다 끝낼때까지 돌기        
    
    
    if int(x) <= t:
        if c == 'L':
            d -= 1
            if d < 0:
                d = 3
        elif c == 'D':
            d += 1
            if d > 3:
                d = 0
        if lp:
            x, c = lp.pop(0)
        else:
            x, c = 21E8, 0
    
    qy, qx = snake[-1][0], snake[-1][1] # 뱀 머리 가져오기
    dy, dx = qy + dir[d][0], qx + dir[d][1] # 다음 뱀 머리 위치 생성

    if 0 <= dy < n and 0 <= dx < n: #뱀 머리가 필드 안에 있어야 함
        if ch[dy][dx] == 0: #몸통이 있는 곳이 아니여야 함
            if [dy+1,dx+1] in ap: #사과가 있는 곳
                ap.pop(ap.index([dy+1,dx+1])) #해당 사과는 먹었음
                ch[dy][dx] = 1 #해당 위치로 머리 이동
                snake.append([dy,dx]) #머리 위치 갱신
            else: #사과가 있는 곳이 아니라면
                ch[dy][dx] = 1 #해당 위치로 머리 이동
                snake.append([dy,dx]) #머리 위치 갱신
                yy, xx = snake.pop(0) #뱀의 꼬리 위치 가져와서
                ch[yy][xx] = 0 #꼬리를 삭제
        else: #몸에 닿으면 끝
            break
    else: #필드 밖으로 나간다면 끝
        break
    
    t += 1 # 시간 초 누적

print(t+1)