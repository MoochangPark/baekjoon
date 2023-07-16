from collections import deque

answer = 0

n = int(input())
l = []

shark = [] # 상어 [y좌표 x좌표 크기]
eat = 0 # 먹은 횟수
fish = [[] for _ in range(7)] # 물고기 크기 별 위치 
fish_count = 0 # 총 물고기 수

# 상어와 물고기 입력 받기
for i in range(n):
    m = list(map(int, input().split()))
    for j in range(n):
        if m[j] == 9: # 상어가 발견될 경우
            shark = [i,j,2] #상어 초기 위치 저장
            m[j] = 0 # 상어의 위치는 0으로 바꿔 두기
        elif 1<= m[j] <= 6: # 물고기를 발견 할 경우
            fish[m[j]].append([i,j]) #물고기 크기 별로 위치 저장
            fish_count += 1 # 물고기 수 증가
            
    l.append(m)

def bfs():
    check = [[0] * n for _ in range(n)] #이동 확인 배열
    can_eat_fish = [] #먹을 수 있는 물고기 저장
    check[shark[0]][shark[1]] = 1
    #움직이기 시작
    while q:
        qy, qx, size, move = q.popleft() #상어 정보 가져오기
        # check[qy][qx] = 1 #상어의 시작 위치를 이동 확인 배열에 저장

        # 상 하 좌 우로 이동 가능
        for dy, dx in [(qy-1,qx),(qy,qx-1),(qy+1,qx),(qy,qx+1)]:
            if 0 <= dy < n and 0 <= dx < n: # 맵을 벗어나지 않는다면
                if check[dy][dx] == 0: # 상어가 간 곳이 아니라면
                    
                    if l[dy][dx] == 0: # 만약 그곳이 빈 곳이라면
                        check[dy][dx] = 1 # 간 곳을 기록
                        q.append([dy, dx, size, move + 1]) # 해당 위치로 이동
                    
                    elif 1<=l[dy][dx]<=6: # 만약 그곳에 물고기가 있다면
                        
                        if l[dy][dx] < size: # 물고기가 상어 크기보다 작다면
                            can_eat_fish.append([dy,dx,move+1]) # 먹을 수 있는 물고기로 저장
                            check[dy][dx] = 1 # 간 곳을 기록
                            q.append([dy, dx, size, move + 1]) # 해당 위치로 이동
                        
                        elif l[dy][dx] == size: # 만약 크기가 같다면 먹을 수는 없음
                            check[dy][dx] = 1 # 간 곳을 기록
                            q.append([dy, dx, size, move + 1]) # 해당 위치로 이동
    
    return can_eat_fish # 먹을 수 있는 물고기들 반환


while True:
    can_eat_fish = [] #먹을 수 있는 물고기
    q = deque()
    
    # 상어의 위치에서 시작
    q.append([shark[0], shark[1], shark[2], 0]) # [y좌표 x좌표 크기 이동 수]
    can_eat_fish = bfs() # 가까운 물고기 찾기 시작
    
    # 만약 먹을 물고기가 없으면 엄마상어 호출
    if fish_count == 0 or len(can_eat_fish) == 0:
        break
    
    can_eat_fish.sort(key=lambda x : (x[2], x[0], x[1])) # 물고기 조건에 따라 정렬

    # 정렬 후에는 맨 앞의 물고기가 가장 가까운 먹이
    answer += can_eat_fish[0][2] # 해당 물고기 먹으러 간 거리 누적
    fish_count -= 1 # 물고기 수 하나 감소
    l[can_eat_fish[0][0]][can_eat_fish[0][1]] = 0 # 해당 위치의 물고기 삭제
    eat += 1 # 상어가 먹은 물고기 1 증가
    
    # 상어가 크기 만큼 먹었다면 크기 증가, 아니면 유지
    if eat == shark[2]:
        shark[2] += 1
        eat = 0
    
    # 상어의 위치를 먹은 물고기의 위치로 갱신 및 몸 크기 갱신
    shark = [can_eat_fish[0][0], can_eat_fish[0][1], shark[2]]

print(answer)