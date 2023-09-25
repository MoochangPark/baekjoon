# 땅은 n*n
# m 개의 나무 사서 심음 
# 칸은 r,c 로 구분
# 초기 양분은 칸마다 5
# 한 칸에 여러 나무 심기 가능
# 봄 - 나무가 나이만큼 양분먹고 나이 1 증가, 나이 어린 나무부터 자람, 양분 부족하면 사망
# 여름 - 죽은 나무가 양분, 나이 // 2 값이 해당 칸 양분에 추가
# 가을 - 나무 번식, 나이가 5의 배수, 인접한 8개 칸에 나이 1인 나무 생성
# 겨울 - 모든 땅에 A[r][c] 만큼 양분 추가
# 결과는 k년 후 살아있는 나무 수 



n, m, k = map(int, input().split())

l = [[5] * n for _ in range(n)] #기본 땅

A = [list(map(int, input().split())) for _ in range(n)] #로봇이 줄 양분

T = [[[] for _ in range(n)] for _ in range(n)] #살아있는 나무들
D = [[[] for _ in range(n)] for _ in range(n)] #죽은 나무들
for _ in range(m):
    r, c, age = map(int, input().split())
    T[r-1][c-1].append(age)

dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]

answer = 0 #정답

def spring():
    for i in range(n):
        for j in range(n):
            if T[i][j]:
                T[i][j].sort() #어린 나무부터
                for _ in range(len(T[i][j])):
                    t = T[i][j].pop(0)
                    if l[i][j] >= t:
                        l[i][j] -= t #나이만큼 양분 먹기
                        t += 1 #나이 1 증가
                        T[i][j].append(t) #살았으니 다시 산 나무로 등록
                    else:
                        D[i][j].append(t) #죽었으니 죽은 나무로 등록

def summer():
    for i in range(n):
        for j in range(n):
            if D[i][j]:
                for _ in range(len(D[i][j])):
                    d = D[i][j].pop() #죽은 나무들
                    l[i][j] += d//2 #나이//2만큼 양분에 추가

def fall():
    for i in range(n):
        for j in range(n):
            if T[i][j]:
                for u in range(len(T[i][j])):
                    if T[i][j][u] % 5 == 0: #산 나무 중 5의 배수 나이면
                        for k in range(8): #8 방향으로
                            y = i+dy[k]
                            x = j+dx[k]
                            if 0 <= y < n and 0 <= x < n: #땅을 벗어나지 않는 선에서
                                T[y][x].append(1) #나이 1인 나무 번식
                    
def winter():
    for i in range(n):
        for j in range(n):
            l[i][j] += A[i][j]

for _ in range(k): #k 년 후
    spring()
    summer()
    fall()
    winter()

for i in range(n):
    for j in range(n):
        answer += len(T[i][j])

print(answer)