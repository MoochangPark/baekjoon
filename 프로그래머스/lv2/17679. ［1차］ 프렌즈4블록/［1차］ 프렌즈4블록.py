def solution(n, m, b):
    answer = 0
    for i in range(len(b)):
        b[i] = list(b[i])
        
    finish = True
    while finish:
        # ch = [[0] * m for _ in range(n)]
        #2*2 찾기
        s = []
        for i in range(n-1):
            for j in range(m-1):
                if b[i][j] != '0':
                    if b[i][j] == b[i][j+1] and b[i][j] == b[i+1][j] and b[i][j] == b[i+1][j+1]:
                        for k in ([i,j], [i,j+1], [i+1,j], [i+1,j+1]):
                            if k not in s:
                                s.append(k)
                            

            
        # 개수 저장 및 지우기
        answer += len(s)
        for i in s:
            b[i[0]][i[1]] = '0'
            
        
        # print(s)
        # for i in range(len(b)):
        #     print(*b[i])
        # print('---------')
        
        #떨어지기
        for i in range(m):
            left = n-1
            right = left
            while left > 0:
                if b[left][i] != '0':
                    left -= 1
                    right -= 1
                else:
                    while right > 0 and b[right][i] == '0':
                        right -= 1
                    b[left][i], b[right][i] = b[right][i], b[left][i]
                    left -= 1
                    right = left
        
        # for i in range(len(b)):
        #     print(*b[i])
        # print("=========")
        
        if len(s) == 0:
            finish = False
        
        # finish = False
    
    return answer