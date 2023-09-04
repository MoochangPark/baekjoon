import heapq

T = int(input()) #입력데이터 수

for _ in range(T):

    Q = [] #최소힙
    rQ = [] #최대힙

    k = int(input()) #연산 개수
    v = [0] * (k+1)

    for i in range(k):
        a, b = input().split() #a는 str, b는 int로 변환 필요

        if a == 'I':
            heapq.heappush(Q, (int(b), i))
            heapq.heappush(rQ, (-int(b), i))
            v[i] = 1 #해당 순서로 들어온 값 있음을 표시

        else:
            if b == '-1':
                while Q and v[Q[0][1]] == 0:
                    heapq.heappop(Q)
                if Q:
                    v[Q[0][1]] = 0
                    heapq.heappop(Q)
            else:
                while rQ and v[rQ[0][1]] == 0:
                    heapq.heappop(rQ)
                if rQ:
                    v[rQ[0][1]] = 0
                    heapq.heappop(rQ)
    
    while Q and v[Q[0][1]] == 0:
        heapq.heappop(Q)
    while rQ and v[rQ[0][1]] == 0:
        heapq.heappop(rQ)

    if not Q and not rQ:
        print("EMPTY")
    
    else:
        a = -rQ[0][0]
        b = Q[0][0]
        print(a, b)