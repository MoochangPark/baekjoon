A, B = map(str, input().split())

if len(A) > len(B):
    A, B = B, A

cnt = 0

mins = 99999

def check(C):
    global cnt
    dif = 0
    for i in range(len(C)):
        if A[i] != C[i]:
            dif += 1
    return dif

for i in range(len(B) - len(A) + 1):
    t = check(B[i:i+len(A)])

    mins = min(mins, cnt + t)

print(mins)