n, m, M, T, R = map(int, input().split()) #운동 N분, 초기 맥박, 기준 맥박, 운동 증가, 휴식 감소

answer = 0
mac = m
t = 0
if m+T > M:
    print(-1)
else:
    while True:
        if answer >= n:
            print(t)
            break
        if mac < m:
            mac = m
        if mac + T > M:
            mac -= R
        else:
            mac += T
            answer += 1
        t += 1