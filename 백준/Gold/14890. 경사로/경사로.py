n, l = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

def LtoR(line):
    global n, l
    ch = [0] * n
    for i in range(n - 1):
        if abs(arr[line][i] - arr[line][i+1]) > 1:
            return False
        if arr[line][i] == arr[line][i+1]:
            continue
        elif arr[line][i] > arr[line][i+1]: # 경사가 내려갈 때
            for j in range(i+1, i+1+l):
                if 0 <= j < n:
                    if arr[line][i+1] != arr[line][j]:
                        return False
                    if ch[j]:
                        return False
                    ch[j] = 1
                else:
                    return False
        else: # 경사가 올라갈 때
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if arr[line][i] != arr[line][j]:
                        return False
                    if ch[j]:
                        return False
                    ch[j] = 1
                else:
                    return False
    return True

def TtoB(line):
    global n, l
    ch = [0] * n
    for i in range(n - 1):
        if abs(arr[i][line] - arr[i+1][line]) > 1:
            return False
        if arr[i][line] == arr[i+1][line]:
            continue
        elif arr[i][line] > arr[i+1][line]: # 경사가 내려갈 때
            for j in range(i+1, i+1+l):
                if 0 <= j < n:
                    if arr[i+1][line] != arr[j][line]:
                        return False
                    if ch[j]:
                        return False
                    ch[j] = 1
                else:
                    return False
        else: # 경사가 올라갈 때
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if arr[i][line] != arr[j][line]:
                        return False
                    if ch[j]:
                        return False
                    ch[j] = 1
                else:
                    return False
    return True


answer = 0

for i in range(n):
    if LtoR(i):
        answer += 1
    if TtoB(i):
        answer += 1

print(answer)