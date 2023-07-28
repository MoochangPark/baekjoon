from collections import deque

l = [deque(list(input())) for _ in range(4)]
# 2와 6을 체크

k = int(input())

for _ in range(k):
    mem = []
    for i in range(4):
        mem.append([l[i][2], l[i][6]])
        
    mm, dd = map(int, input().split()) # 1 시계 -1 반시계
    mm -= 1


    for i in range(mm,0,-1):
        if mem[i][1] != mem[i-1][0]:
            if (mm-i-1) % 2 == 0:
                l[i-1].rotate(dd)
            else:
                l[i-1].rotate(-dd)
        else:
            break


    for i in range(mm,3):
        if mem[i][0] != mem[i+1][1]:
            if (mm-i+1) % 2 == 0:
                l[i+1].rotate(dd)
            else:
                l[i+1].rotate(-dd)
        else:
            break
    
    l[mm].rotate(dd)

answer = 0
t = [1, 2, 4, 8]
for i in range(4):
    a = t[i] if l[i][0] == '1' else 0
    answer += a
print(answer)