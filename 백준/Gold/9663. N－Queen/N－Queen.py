n = int(input())

answer = 0

zips = [0] * n #각 열번호는 행의 자리, 값은 열의 자리를 의미
ch = [0] * n #해당 열에 놓을 수 있는지 확인

def check(q):
    for i in range(q):
        #대각선의 조건은 의외로 쉽다. 1,1과 2,2를 생각해보면  각 행과 각 열의 차가 같은 애들임
        if (q == i) or (q-i == abs(zips[q] - zips[i])): # 같은 열에 있거나 대각선이 같다면
            return False
    return True

def dfs(q):
    global answer
    if q == n:
        answer += 1
        return
    
    for i in range(n): # 각 열마다 확인
        if ch[i] == 0:
            zips[q] = i #q번째 퀸은 행이 q이고, 열을 찾기 위해 i를 바꿔간다

            if check(q):
                ch[i] = 1
                dfs(q + 1)
                ch[i] = 0

dfs(0) # 놓인 퀸의 행

print(answer)